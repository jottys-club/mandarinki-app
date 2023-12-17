from sqlalchemy import Integer, Column, String, Float, Text, UUID

from database.database import Base


class MLLog(Base):
    __tablename__ = 'ml_logs'

    uuid = Column(UUID, primary_key=True)
    id = Column(Integer)
    gender = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)
    reg_region_nm = Column(String, nullable=True)
    cnt_tr_all_3m = Column(Integer, nullable=True)
    cnt_tr_top_up_3m = Column(Integer, nullable=True)
    cnt_tr_cash_3m = Column(Integer, nullable=True)
    cnt_tr_buy_3m = Column(Integer, nullable=True)
    cnt_tr_mobile_3m = Column(Integer, nullable=True)
    cnt_tr_oil_3m = Column(Integer, nullable=True)
    cnt_tr_on_card_3m = Column(Integer, nullable=True)
    cnt_tr_service_3m = Column(Integer, nullable=True)
    cnt_zp_12m = Column(Integer, nullable=True)
    sum_zp_12m = Column(Float, nullable=True)
    limit_exchange_count = Column(Integer, nullable=True)
    max_outstanding_amount_6m = Column(Integer, nullable=True)
    avg_outstanding_amount_3m = Column(Integer, nullable=True)
    cnt_dep_act = Column(Integer, nullable=True)
    sum_dep_now = Column(Float, nullable=True)
    avg_dep_avg_balance_1month = Column(Float, nullable=True)
    max_dep_avg_balance_3month = Column(Float, nullable=True)
    app_vehicle_ind = Column(Integer, nullable=True)
    app_position_type_nm = Column(String, nullable=True)
    visit_purposes = Column(String, nullable=True)
    qnt_months_from_last_visit = Column(Integer, nullable=True)
    super_clust = Column(String, nullable=True)
    product = Column(String, nullable=True)
    channel = Column(String, nullable=True)
    generated_text = Column(Text, nullable=True)
    model_coefficient = Column(Float, nullable=True)
