from pydantic import BaseModel
from typing import Optional

class DeviceInput(BaseModel):
    battery_power: int
    blue: int  
    clock_speed: float
    dual_sim: int  
    fc: float
    four_g: int  
    int_memory: int
    m_dep: float
    mobile_wt: float
    n_cores: int
    pc: float
    px_height: int
    px_width: int
    ram: int
    sc_h: float
    sc_w: float
    talk_time: int
    three_g: int  
    touch_screen: int  
    wifi: int  

class PredictionOutput(BaseModel):
    predicted_price: int  