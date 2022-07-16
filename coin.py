from profile import profile
from convert import convert

class coin:
    def __init__(self, profile_id:str):
        self.id = profile_id

    def add(self, money:int):
        money = abs(money)
        m_profile = profile(self.id).get()
        new_money = m_profile["money"] + money
        m_profile["money"] = new_money
        profile(self.id).change(m_profile)
    
    def remove(self, money:int):
        money = abs(money)
        m_profile = profile(self.id).get()
        if m_profile["money"] >= money:
            new_money = m_profile["money"] - money
            m_profile["money"] = new_money
            profile(self.id).change(m_profile)
    
    def transfer(self, target_id:str, money:int):
        money = abs(money)
        m_profile = profile(self.id).get()
        if m_profile["money"] >= money:
            t_profile = profile(target_id).get()
            m_profile["money"] = m_profile["money"] - money
            t_profile["money"] = t_profile["money"] + money
            profile(self.id).change(m_profile)
            profile(target_id).change(t_profile)