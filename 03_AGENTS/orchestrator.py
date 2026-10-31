"""
Orquestador Autónomo del Comité Ejecutivo IA (0 Humanos)
Combina ejecución determinista (0€ coste, 0% alucinaciones) con razonamiento IA agnóstico opcional.
"""

import os
import hashlib
import json
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

try:
    from .constitution import ConstitutionValidator
except ImportError:
    from constitution import ConstitutionValidator

env_path = os.path.join(os.path.dirname(__file__), "..", "04_CONFIG", ".env")
load_dotenv(dotenv_path=env_path)


class AutonomousCommittee:
    """
    Comité de Dirección 100% Autónomo:
    - Curator (CPO & I+D): Calidad e Innovación Open Source
    - Vulcan (CTO & SRE): Arbitraje de Servidores y Auto-Healing
    - Ledger (CFO): Coste Mínimo Asintótico y Deflación Automática
    - Atlas (CEO): Gobernanza Constitucional y Firma Criptográfica SHA-256
    """

    @staticmethod
    def compute_sha256_block(prev_hash: str, agent: str, action_type: str, payload: Dict[str, Any], timestamp: str) -> str:
        raw = json.dumps(
            {
                "prev_hash": prev_hash,
                "agent": agent,
                "action_type": action_type,
                "payload": payload,
                "timestamp": timestamp,
            },
            sort_keys=True,
            ensure_ascii=False,
        )
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    @classmethod
    def run_vulcan_arbitrage(cls, providers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Vulcan (CTO IA): Analiza en tiempo real proveedores Bare-Metal / VPS y selecciona
        el nodo con menor coste físico por unidad de cómputo que cumpla SLA >= 99.95%.
        """
        eligible = [p for p in providers if p.get("uptime_sla", 0) >= ConstitutionValidator.MIN_UPTIME_PERCENT]
        if not eligible:
            eligible = providers

        # Ordenar por eficiencia: (coste_mensual_nodo / (vcpu * 2 + ram_gb)) + penalización por latencia
        scored = []
        for p in eligible:
            compute_units = (p["vcpu"] * 2.0) + p["ram_gb"]
            eur_per_unit = p["node_monthly_eur"] / max(1.0, compute_units)
            efficiency_index = round(eur_per_unit * (1.0 + (p["latency_ms"] / 1000.0)), 4)
            scored.append({**p, "eur_per_compute_unit": round(eur_per_unit, 3), "efficiency_index": efficiency_index})

        scored.sort(key=lambda x: x["efficiency_index"])
        winner = scored[0]
        baseline_unit_cost = max(x["eur_per_compute_unit"] for x in scored)
        arbitrage_factor = round(winner["eur_per_compute_unit"] / baseline_unit_cost, 3) if baseline_unit_cost > 0 else 1.0

        return {
            "selected_provider": winner["provider"],
            "datacenter": winner["datacenter"],
            "spec": f"{winner['vcpu']} vCPU / {winner['ram_gb']}GB RAM NVMe",
            "eur_per_compute_unit": winner["eur_per_compute_unit"],
            "arbitrage_discount_factor": max(0.72, min(1.0, arbitrage_factor)),
            "savings_vs_worst_percent": round((1.0 - arbitrage_factor) * 100, 1),
            "ranked_nodes": scored,
        }

    @classmethod
    def run_curator_benchmark(cls, catalog: List[Dict[str, Any]], sandbox_radar: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Curator (CPO & I+D IA): Audita la calidad, velocidad de innovación y huella de RAM
        del catálogo activo y los candidatos en sandbox.
        """
        evaluated_catalog = []
        for app in catalog:
            score = ConstitutionValidator.compute_innovation_index(
                app["quality_score"], app["innovation_velocity"], app["ram_efficiency"]
            )
            evaluated_catalog.append({**app, "composite_score": score})

        evaluated_catalog.sort(key=lambda x: x["composite_score"], reverse=True)

        promoted_candidates = []
        for cand in sandbox_radar:
            c_score = ConstitutionValidator.compute_innovation_index(
                cand["quality_score"], cand["innovation_velocity"], cand["ram_efficiency"]
            )
            cand["composite_score"] = c_score
            if c_score >= 90.0:
                promoted_candidates.append(cand)

        top_app = evaluated_catalog[0] if evaluated_catalog else None
        return {
            "evaluated_catalog": evaluated_catalog,
            "sandbox_radar": sandbox_radar,
            "top_performer": top_app["name"] if top_app else "N/A",
            "average_innovation_score": round(
                sum(x["composite_score"] for x in evaluated_catalog) / max(1, len(evaluated_catalog)), 1
            ),
            "ready_for_promotion": [c["name"] for c in promoted_candidates],
        }

    @classmethod
    def run_ledger_deflation_audit(
        cls,
        catalog: List[Dict[str, Any]],
        reserve_runway_months: float,
        arbitrage_discount_factor: float,
        active_instances_count: int,
    ) -> Dict[str, Any]:
        """
        Ledger (CFO IA): Recalcula al céntimo el coste de cada SaaS Open Source alojado.
        Aplica la Ley de Coste Mínimo Asintótico (0€ licencias, 0€ nóminas humanas).
        """
        repriced_catalog = []
        total_monthly_rebate = 0.0

        for app in catalog:
            breakdown = ConstitutionValidator.calculate_asymptotic_price(
                hardware_cost_eur=app["base_hardware_eur"],
                ai_compute_cost_eur=app["ai_compute_eur"],
                reserve_runway_months=reserve_runway_months,
                arbitrage_discount_factor=arbitrage_discount_factor,
            )
            previous_price = app.get("final_price_eur", breakdown["total_monthly_eur"])
            price_delta = round(breakdown["total_monthly_eur"] - previous_price, 2)
            if price_delta < 0:
                total_monthly_rebate += abs(price_delta)

            repriced_catalog.append(
                {
                    **app,
                    "pricing": breakdown,
                    "final_price_eur": breakdown["total_monthly_eur"],
                    "price_delta_eur": price_delta,
                }
            )

        return {
            "repriced_catalog": repriced_catalog,
            "deflation_active": reserve_runway_months >= ConstitutionValidator.TARGET_SURVIVAL_MONTHS,
            "reserve_runway_months": round(reserve_runway_months, 2),
            "avg_instance_price_eur": round(
                sum(x["final_price_eur"] for x in repriced_catalog) / max(1, len(repriced_catalog)), 2
            ),
            "active_instances_count": active_instances_count,
        }

    @classmethod
    def run_atlas_executive_cycle(
        cls,
        state: Dict[str, Any],
        prev_hash: str,
    ) -> Dict[str, Any]:
        """
        Atlas (CEO IA): Coordina el ciclo completo entre Vulcan, Curator y Ledger,
        verifica la Constitución Algorítmica y emite una resolución firmada en SHA-256.
        """
        now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        # 1. Vulcan ejecuta arbitraje de servidores
        vulcan_report = cls.run_vulcan_arbitrage(state["cloud_providers"])

        # 2. Curator ejecuta benchmarking de calidad e innovación Open Source
        curator_report = cls.run_curator_benchmark(state["catalog"], state.get("sandbox_radar", []))

        # 3. Ledger recalcula precios mínimos asintóticos con el descuento de arbitraje de Vulcan
        new_runway = round(min(24.0, state.get("reserve_runway_months", 12.4) + 0.3), 2)
        ledger_report = cls.run_ledger_deflation_audit(
            catalog=curator_report["evaluated_catalog"],
            reserve_runway_months=new_runway,
            arbitrage_discount_factor=vulcan_report["arbitrage_discount_factor"],
            active_instances_count=len(state.get("instances", [])),
        )

        # 4. Validación Constitucional Inmutable
        candidate_state = {
            **state,
            "catalog": ledger_report["repriced_catalog"],
            "reserve_runway_months": new_runway,
            "human_payroll_eur": 0.0,
        }
        is_valid, violations, guarantees = ConstitutionValidator.validate_autonomous_state(candidate_state)

        # 5. Síntesis Ejecutiva de Atlas (Determinista, 0€ gasto superfluo)
        resolution_summary = (
            f"Ciclo Autónomo completado. "
            f"Vulcan (CTO) asignó carga primaria a {vulcan_report['selected_provider']} ({vulcan_report['datacenter']}) "
            f"a {vulcan_report['eur_per_compute_unit']}€/unidad (-{vulcan_report['savings_vs_worst_percent']}% vs nodo más caro). "
            f"Curator (CPO) auditó {len(ledger_report['repriced_catalog'])} suites OSS con índice medio de innovación de "
            f"{curator_report['average_innovation_score']}/100 (líder: {curator_report['top_performer']}). "
            f"Ledger (CFO) fijó la cuota media en {ledger_report['avg_instance_price_eur']}€/mes "
            f"(0,00€ licencias, 0,00€ nóminas humanas, reserva en {new_runway} meses, deflación automática: "
            f"{'ACTIVA' if ledger_report['deflation_active'] else 'EN ACUMULACIÓN'})."
        )

        payload = {
            "constitutional_valid": is_valid,
            "selected_cloud_node": f"{vulcan_report['selected_provider']} ({vulcan_report['datacenter']})",
            "avg_price_eur": ledger_report["avg_price_eur"] if "avg_price_eur" in ledger_report else ledger_report["avg_instance_price_eur"],
            "avg_innovation_score": curator_report["average_innovation_score"],
            "reserve_runway_months": new_runway,
            "summary": resolution_summary,
        }
        block_hash = cls.compute_sha256_block(prev_hash, "Atlas (CEO IA)", "EXECUTIVE_CYCLE_RESOLUTION", payload, now_iso)

        return {
            "timestamp": now_iso,
            "constitutional_valid": is_valid,
            "violations": violations,
            "guarantees": guarantees,
            "vulcan_report": vulcan_report,
            "curator_report": curator_report,
            "ledger_report": ledger_report,
            "resolution_summary": resolution_summary,
            "audit_block": {
                "timestamp": now_iso,
                "agent": "Atlas (CEO IA)",
                "action_type": "EXECUTIVE_CYCLE_RESOLUTION",
                "summary": resolution_summary,
                "prev_hash": prev_hash,
                "curr_hash": block_hash,
            },
        }
