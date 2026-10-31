"""
Motor de la Constitución Algorítmica (0 Humanos)
Cuatro invariantes inmutables en código que gobiernan la empresa autónoma de IA.
"""

from typing import Dict, Any, Tuple, List

APPROVED_OSI_LICENSES = {"MIT", "Apache-2.0", "AGPL-3.0", "GPL-3.0", "BSD-3-Clause", "MPL-2.0"}


class ConstitutionValidator:
    MIN_UPTIME_PERCENT = 99.95
    TARGET_SURVIVAL_MONTHS = 12.0
    MIN_MERITOCRACY_SCORE = 82.0
    BASE_RESERVE_RATE = 0.12  # 12% para fondo de supervivencia e I+D cuando el colchón < 12 meses
    DEFLATION_RESERVE_RATE = 0.03  # Cae al 3% automáticamente al superar el colchón de 12 meses

    @classmethod
    def calculate_asymptotic_price(
        cls,
        hardware_cost_eur: float,
        ai_compute_cost_eur: float,
        reserve_runway_months: float,
        arbitrage_discount_factor: float = 1.0,
    ) -> Dict[str, Any]:
        """
        Invariante 2: Ley de Coste Mínimo Asintótico (Deflación Automática).
        Calcula al céntimo el coste puro de alojamiento sin márgenes comerciales ni licencias.
        """
        effective_hw = round(hardware_cost_eur * arbitrage_discount_factor, 2)
        base_operational = round(effective_hw + ai_compute_cost_eur, 2)

        deflation_active = reserve_runway_months >= cls.TARGET_SURVIVAL_MONTHS
        applied_reserve_rate = cls.DEFLATION_RESERVE_RATE if deflation_active else cls.BASE_RESERVE_RATE

        # Si el runway supera ampliamente los 12 meses, el excedente reduce aún más la cuota
        rebate_eur = 0.0
        if reserve_runway_months > cls.TARGET_SURVIVAL_MONTHS:
            excess_months = min(reserve_runway_months - cls.TARGET_SURVIVAL_MONTHS, 12.0)
            rebate_eur = round(base_operational * (excess_months * 0.008), 2)

        reserve_contribution = round(max(0.10, base_operational * applied_reserve_rate - rebate_eur), 2)
        total_exact_price = round(effective_hw + ai_compute_cost_eur + reserve_contribution, 2)

        return {
            "hardware_cost_eur": effective_hw,
            "ai_compute_cost_eur": round(ai_compute_cost_eur, 2),
            "reserve_rnd_eur": reserve_contribution,
            "license_cost_eur": 0.00,
            "human_payroll_eur": 0.00,
            "deflation_active": deflation_active,
            "deflation_rebate_eur": rebate_eur,
            "total_monthly_eur": total_exact_price,
        }

    @classmethod
    def compute_innovation_index(
        cls, quality_score: float, innovation_velocity: float, ram_efficiency: float
    ) -> float:
        """
        Invariante 4: Índice compuesto de Meritocracia e Innovación (0-100).
        Pondera calidad de ingeniería (40%), velocidad de innovación (40%) y eficiencia de recursos (20%).
        """
        return round(
            (quality_score * 0.40) + (innovation_velocity * 0.40) + (ram_efficiency * 0.20),
            1,
        )

    @classmethod
    def validate_autonomous_state(cls, state: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
        """
        Audita en tiempo real el cumplimiento de las 4 Invariantes Constitucionales.
        Devuelve: (es_valido, violaciones, garantias_activas)
        """
        violations: List[str] = []
        guarantees: List[str] = []

        # Invariante 1: Soberanía Open Source (0€ en licencias, 100% OSI)
        non_free = [
            app["name"]
            for app in state.get("catalog", [])
            if app.get("license") not in APPROVED_OSI_LICENSES or app.get("license_cost_eur", 0.0) > 0
        ]
        if non_free:
            violations.append(
                f"[INVARIANTE 1 VIOLADA]: Detectado software con licencia privativa o coste de licencia: {', '.join(non_free)}."
            )
        else:
            guarantees.append(
                "INVARIANTE 1 (Soberanía Open Source): 100% código libre verificado (OSI). 0,00€ en licencias. Exportación libre activa."
            )

        # Invariante 2: Coste Mínimo Asintótico y Deflación
        runway = state.get("reserve_runway_months", 0.0)
        human_payroll = state.get("human_payroll_eur", 0.0)
        if human_payroll > 0:
            violations.append(
                f"[INVARIANTE 2 VIOLADA]: Detectado gasto burocrático humano ({human_payroll}€). La estructura debe ser 100% autónoma."
            )
        elif runway >= cls.TARGET_SURVIVAL_MONTHS:
            guarantees.append(
                f"INVARIANTE 2 (Deflación Automática ACTIVA): Reserva en {runway} meses (>=12m). Tasa de reserva reducida al 3% y excedente devuelto en rebaja directa de cuota."
            )
        else:
            guarantees.append(
                f"INVARIANTE 2 (Coste Mínimo de Subsistencia): Reserva en {runway} meses. Cuota = Hierro + Cómputo IA + 12% Fondo Supervivencia."
            )

        # Invariante 3: Estabilidad e Infraestructura (Veto del CTO IA)
        uptime = state.get("uptime_percent", 100.0)
        critical_cves = state.get("critical_cves", 0)
        if uptime < cls.MIN_UPTIME_PERCENT or critical_cves > 0:
            violations.append(
                f"[INVARIANTE 3 — VETO DE VULCAN ACTIVADO]: Uptime ({uptime}%) < {cls.MIN_UPTIME_PERCENT}% o CVEs críticos ({critical_cves}) > 0. "
                "Congelados despliegues experimentales; 100% del cómputo en auto-reparación."
            )
        else:
            guarantees.append(
                f"INVARIANTE 3 (Estabilidad CTO): Uptime global en {uptime}% (>=99.95%), 0 CVEs críticos sin parchear."
            )

        # Invariante 4: Meritocracia e Innovación Continua (CPO IA)
        low_quality = [
            app["name"]
            for app in state.get("catalog", [])
            if app.get("composite_score", 100.0) < cls.MIN_MERITOCRACY_SCORE
        ]
        if low_quality:
            violations.append(
                f"[INVARIANTE 4 VIOLADA]: Software por debajo del umbral de calidad/innovación ({cls.MIN_MERITOCRACY_SCORE}): {', '.join(low_quality)}."
            )
        else:
            guarantees.append(
                f"INVARIANTE 4 (Meritocracia e Innovación): Todo el catálogo supera el índice compuesto >={cls.MIN_MERITOCRACY_SCORE}/100 en sandbox."
            )

        return len(violations) == 0, violations, guarantees
