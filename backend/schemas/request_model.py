from pydantic import BaseModel


class UserFeatures(BaseModel):
    gender: int | None
    age: int | None
    reg_region_nm: str | None
    cnt_tr_all_3m: int | None
    cnt_tr_top_up_3m: int | None
    cnt_tr_cash_3m: int | None
    cnt_tr_buy_3m: int | None
    cnt_tr_mobile_3m: int | None
    cnt_tr_oil_3m: int | None
    cnt_tr_on_card_3m: int | None
    cnt_tr_service_3m: int | None
    cnt_zp_12m: int | None
    sum_zp_12m: float | None
    limit_exchange_count: int | None
    max_outstanding_amount_6m: int | None
    avg_outstanding_amount_3m: int | None
    cnt_dep_act: int | None
    sum_dep_now: float | None
    avg_dep_avg_balance_1month: float | None
    max_dep_avg_balance_3month: float | None
    app_vehicle_ind: int | None
    app_position_type_nm: str | None
    visit_purposes: str | None
    qnt_months_from_last_visit: int | None
    super_clust: str | None


class Request(BaseModel):
    id: int
    user_features: UserFeatures
    product: str
    channel: str
