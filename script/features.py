
import numpy as np
import random
class Intelligent:
    """智慧种族的静态属性容器，包含种族、职业、属性等不变信息"""
    
    def __init__(self, race, profession, level=1):
        # ===== 基本身份信息 =====
        self.race = race  # 种族:0,1,2,3,4,5,6分别对应人类、精灵、龙族、不死族、矮人、人鱼、渡鸦人
        self.profession = profession  # 职业:0,1,2,3,4,5,6分别对应法师、牧师、圣骑士、战士、炼金术士、德鲁伊、普通士兵
        self.level = level  # 冒险者阶次: 0,1,2,3分别对应平民、新手、老兵、大师
        
        # ===== 基础属性值 =====
        self.attributes = {
            'endurance': 0,      # 体能
            'concentration': 0,  # 专注力
            'strength': 0,       # 力量
            'agility': 0,        # 敏捷
            'intelligence': 0,   # 智力
            'faith': 0,          # 信仰
            'insight': 0,        # 洞察
            'charisma': 0,       # 魅力
            'luck': 0  ,          # 幸运
            'light_shield': 0   # 光明护盾
        }
        
        # ===== 技能代号 =====
        self.profession_skill_ids = []  # 职业技能代号列表
        self.available_skill_ids = []   # 所有可用技能代号
        
        # 初始化属性
        self.initialize_attributes()
        # 初始化技能
        self.initialize_skills()
    
    def num_to_race(self):
        """将种族数字代号转换为字符串表示"""
        race_dict = {
            0: 'human',
            1: 'elf',
            2: 'dragon',
            3: 'undead',
            4: 'dwarf',
            5: 'mermaid',
            6: 'raven'
        }
        return race_dict.get(self.race, "unknown")
    def num_to_profession(self):
        """将职业数字代号转换为字符串表示"""
        profession_dict = {
            0: 'mage',
            1: 'priest',
            2: 'paladin',
            3: 'warrior',
            4: 'alchemist',
            5: 'druid',
            6: 'soldier'
        }
        return profession_dict.get(self.profession, "unknown")
    
    def initialize_attributes(self):
        """根据种族、职业和等级初始化属性"""
        # 种族基础属性
        race_base_attributes = {
            'human': {'endurance': 4, 'concentration': 4, 'strength': 3, 'agility': 3, 
                     'intelligence': 3, 'faith': 3, 'insight': 3, 'charisma': 3, 'luck': 3, 'light_shield': 0},
            'elf': {'endurance': 2, 'concentration': 3, 'strength': 2, 'agility': 3,
                   'intelligence': 5, 'faith': 3, 'insight': 4, 'charisma': 4, 'luck': 3, 'light_shield': 0},
            'dragon': {'endurance': 5, 'concentration': 3, 'strength': 3, 'agility': 2,
                      'intelligence': 4, 'faith': 5, 'insight': 2, 'charisma': 2, 'luck': 1, 'light_shield': 0},
            'undead': {'endurance': 2, 'concentration': 3, 'strength': 2, 'agility': 4,
                      'intelligence': 4, 'faith': 1, 'insight': 5, 'charisma': 5, 'luck': 5, 'light_shield': 0},
            'dwarf': {'endurance': 5, 'concentration': 5, 'strength': 4, 'agility': 1,
                     'intelligence': 3, 'faith': 3, 'insight': 3, 'charisma': 1, 'luck': 4, 'light_shield': 0},
            'mermaid': {'endurance': 1, 'concentration': 3, 'strength': 2, 'agility': 5,
                       'intelligence': 4, 'faith': 3, 'insight': 3, 'charisma': 5, 'luck': 3, 'light_shield': 0},
            'raven': {'endurance': 3, 'concentration': 4, 'strength': 3, 'agility': 4,
                     'intelligence': 3, 'faith': 1, 'insight': 5, 'charisma': 3, 'luck': 3, 'light_shield': 0}
        }
        
        # 职业成长属性（上限表）
        profession_growth_max = {
            'mage': {'endurance': 1, 'concentration': 8, 'strength': 0, 'agility': 5,
                    'intelligence': 9, 'faith': 0, 'insight': 6, 'charisma': 0, 'luck': 1, 'light_shield': 1},
            'priest': {'endurance': 3, 'concentration': 4, 'strength': 0, 'agility': 0,
                      'intelligence': 8, 'faith': 9, 'insight': 6, 'charisma': 0, 'luck': 0, 'light_shield': 2},
            'paladin': {'endurance': 7, 'concentration': 4, 'strength': 5, 'agility': 1,
                       'intelligence': 5, 'faith': 6, 'insight': 1, 'charisma': 0, 'luck': 1, 'light_shield': 2},
            'warrior': {'endurance': 8, 'concentration': 0, 'strength': 9, 'agility': 6,
                       'intelligence': 0, 'faith': 0, 'insight': 3, 'charisma': 0, 'luck': 4, 'light_shield': 1},
            'alchemist': {'endurance': 1, 'concentration': 6, 'strength': 0, 'agility': 5,
                         'intelligence': 9, 'faith': 0, 'insight': 8, 'charisma': 0, 'luck': 1, 'light_shield': 1},
            'druid': {'endurance': 5, 'concentration': 3, 'strength': 0, 'agility': 1,
                     'intelligence': 7, 'faith': 1, 'insight': 5, 'charisma': 7, 'luck': 1, 'light_shield': 1},
            'soldier': {'endurance': 2, 'concentration': 2, 'strength': 2, 'agility': 2,
                        'intelligence': 2, 'faith': 2, 'insight': 2, 'charisma': 2, 'luck': 2, 'light_shield': 0}
        }
        
        # 职业成长属性（下限表）
        profession_growth_min = {
            'mage': {'endurance': 0, 'concentration': 3, 'strength': 0, 'agility': 1,
                    'intelligence': 4, 'faith': 0, 'insight': 2, 'charisma': 0, 'luck': 0, 'light_shield': 0},
            'priest': {'endurance': 0, 'concentration': 1, 'strength': 0, 'agility': 0,
                      'intelligence': 3, 'faith': 4, 'insight': 2, 'charisma': 0, 'luck': 0, 'light_shield': 1},
            'paladin': {'endurance': 4, 'concentration': 0, 'strength': 2, 'agility': 0,
                       'intelligence': 1, 'faith': 3, 'insight': 0, 'charisma': 0, 'luck': 0, 'light_shield': 1},
            'warrior': {'endurance': 3, 'concentration': 0, 'strength': 4, 'agility': 2,
                       'intelligence': 0, 'faith': 0, 'insight': 0, 'charisma': 0, 'luck': 1, 'light_shield': 0},
            'alchemist': {'endurance': 0, 'concentration': 2, 'strength': 0, 'agility': 1,
                         'intelligence': 4, 'faith': 0, 'insight': 3, 'charisma': 0, 'luck': 0, 'light_shield': 0},
            'druid': {'endurance': 2, 'concentration': 0, 'strength': 0, 'agility': 0,
                     'intelligence': 3, 'faith': 0, 'insight': 1, 'charisma': 4, 'luck': 0, 'light_shield': 0},
            'soldier': {'endurance': 1, 'concentration': 1, 'strength': 1, 'agility': 1,
                        'intelligence': 1, 'faith': 1, 'insight': 1, 'charisma': 1, 'luck': 1, 'light_shield': 0}
        }
        
        # 应用种族基础属性
        race_attrs = race_base_attributes.get(self.num_to_race(), {})
        for attr, value in race_attrs.items():
            self.attributes[attr] = value
        
       #计算等级加成，level对应加成次数，每一次加成量是最大值和最小值中间平均分布的随机数四舍五入为整数
        if self.level == 0:
            pass
        else:
            max_growth = profession_growth_max[self.num_to_profession()]
            min_growth = profession_growth_min[self.num_to_profession()]
            for i in range(self.level):
                for attr in self.attributes.keys():
                    growth_increase = random.randint(min_growth[attr], max_growth[attr])
                    self.attributes[attr] += growth_increase
                   
       
        
    
    def initialize_skills(self):
        """根据种族和职业初始化技能代号"""
        # 种族技能代号映射
        racial_skill_map = {
            'human': 101,    # 鼓舞
            'elf': 102,      # 集中精力
            'dragon': 103,   # 龙化
            'undead': 104,   # 破限游走
            'dwarf': 105,    # 武器保养
            'mermaid': 106,  # 潮汐庇护
            'raven': 107     # 干扰
        }
        
        # 职业技能代号映射
        profession_skill_map = {
            'mage': [201, 202],      # 奥术飞弹，魔法护盾
            'priest': [203, 204],    # 治疗术，神圣打击
            'paladin': [205, 206],   # 神圣冲锋，信仰守护
            'warrior': [207, 208],   # 狂暴，破甲打击
            'alchemist': [209, 210], # 元素融合，药剂投掷
            'druid': [211, 212]      # 自然召唤，荆棘缠绕
        }
        
        # 设置种族技能
        self.racial_skill_id = racial_skill_map.get(self.race, 0)
        
        # 设置职业技能
        self.profession_skill_ids = profession_skill_map.get(self.profession, [])
        
        # 所有可用技能
        self.available_skill_ids = [self.racial_skill_id] + self.profession_skill_ids
        

import csv
import os

class Weapon:
    """武器类，从CSV文件加载数据"""
    
    def __init__(self, weapon_id, name, damage_bonus, attribute_modifiers):
        """
        初始化武器
        
        Args:
            weapon_id (int): 武器编号
            name (str): 武器名称
            damage_bonus (list): 伤害加成数组
            attribute_modifiers (list): 属性修正矩阵 2D数组
        """
        self.weapon_id = weapon_id
        self.name = name
        self.damage_bonus = damage_bonus
        self.attribute_modifiers = attribute_modifiers
        
        # 验证数组维度
        self._validate_arrays()
    
    def _validate_arrays(self):
        """验证伤害加成数组和属性修正矩阵的维度"""
        if not self.damage_bonus:
            raise ValueError("伤害加成数组不能为空")
        
        if not self.attribute_modifiers:
            raise ValueError("属性修正矩阵不能为空")
        
        # 检查矩阵是否规整
        row_lengths = [len(row) for row in self.attribute_modifiers]
        if len(set(row_lengths)) != 1 or row_lengths[0] != len(self.damage_bonus):
            raise ValueError("属性修正矩阵的列数必须与伤害加成数组长度一致")
    
    def get_damage_bonus(self, damage_type_index):
        """获取特定伤害类型的加成"""
        if damage_type_index < 0 or damage_type_index >= len(self.damage_bonus):
            return 0
        return self.damage_bonus[damage_type_index]
    
    def get_attribute_modifier(self, attribute_index, damage_type_index):
        """获取特定属性对特定伤害类型的修正值"""
        if (attribute_index < 0 or attribute_index >= len(self.attribute_modifiers) or 
            damage_type_index < 0 or damage_type_index >= len(self.damage_bonus)):
            return 0
        
        return self.attribute_modifiers[attribute_index][damage_type_index]
    
    def calculate_total_damage_bonus(self, attributes, damage_type_index):
        """
        计算总伤害加成（基础加成 + 属性修正）
        
        Args:
            attributes (list): 属性值数组
            damage_type_index (int): 伤害类型索引
        """
        if len(attributes) != len(self.attribute_modifiers):
            raise ValueError(f"属性数组长度({len(attributes)})必须与属性修正矩阵行数({len(self.attribute_modifiers)})一致")
        
        base_bonus = self.get_damage_bonus(damage_type_index)
        attribute_bonus = 0
        
        # 计算属性修正
        for i, attr_value in enumerate(attributes):
            modifier = self.get_attribute_modifier(i, damage_type_index)
            attribute_bonus += attr_value * modifier
        
        return base_bonus + attribute_bonus
    
    def __str__(self):
        return f"Weapon[{self.weapon_id}]: {self.name}"

class WeaponDatabase:
    """武器数据库，从CSV文件加载武器数据"""
    
    def __init__(self, csv_file_path="weapons.csv"):
        self.weapons = {}  # weapon_id -> Weapon对象
        self.csv_file_path = csv_file_path
        self._load_from_csv()
    
    def _parse_array_string(self, array_str, expected_length=None):
        """解析数组字符串（逗号分隔）"""
        try:
            values = [float(x.strip()) for x in array_str.split(",") if x.strip()]
            if expected_length and len(values) != expected_length:
                raise ValueError(f"数组长度应为{expected_length}，实际为{len(values)}")
            return values
        except ValueError as e:
            raise ValueError(f"解析数组字符串失败: {array_str} - {e}")
    
    def _parse_matrix_string(self, matrix_str, expected_rows=None, expected_cols=None):
        """解析矩阵字符串（分号分隔行，逗号分隔列）"""
        try:
            rows = matrix_str.split(";")
            matrix = []
            
            for row in rows:
                if not row.strip():
                    continue
                values = [float(x.strip()) for x in row.split(",") if x.strip()]
                matrix.append(values)
            
            # 验证矩阵维度
            if not matrix:
                raise ValueError("矩阵为空")
            
            # 检查所有行长度是否一致
            row_lengths = [len(row) for row in matrix]
            if len(set(row_lengths)) != 1:
                raise ValueError("矩阵行长度不一致")
            
            if expected_rows and len(matrix) != expected_rows:
                raise ValueError(f"矩阵行数应为{expected_rows}，实际为{len(matrix)}")
            
            if expected_cols and len(matrix[0]) != expected_cols:
                raise ValueError(f"矩阵列数应为{expected_cols}，实际为{len(matrix[0])}")
            
            return matrix
        except ValueError as e:
            raise ValueError(f"解析矩阵字符串失败: {matrix_str} - {e}")
    
    def _load_from_csv(self):
        """从CSV文件加载武器数据"""
        if not os.path.exists(self.csv_file_path):
            raise FileNotFoundError(f"武器数据文件不存在: {self.csv_file_path}")
        
        try:
            with open(self.csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row_num, row in enumerate(reader, start=2):  # 从第2行开始（跳过标题）
                    try:
                        # 解析基本字段
                        weapon_id = int(row['weapon_id'])
                        name = row['name']
                        damage_type_count = int(row['damage_type_count'])
                        
                        # 解析伤害加成数组
                        damage_bonus = self._parse_array_string(
                            row['damage_bonus'], 
                            expected_length=damage_type_count
                        )
                        
                        # 解析属性修正矩阵
                        # 假设有9种属性（对应9行）
                        attribute_modifiers = self._parse_matrix_string(
                            row['attribute_modifiers'],
                            expected_rows=9,  # 9种属性
                            expected_cols=damage_type_count
                        )
                        
                        # 创建武器对象
                        weapon = Weapon(weapon_id, name, damage_bonus, attribute_modifiers)
                        self.weapons[weapon_id] = weapon
                        
                    except (KeyError, ValueError) as e:
                        print(f"警告: 解析第{row_num}行数据失败: {e}")
                        continue
                        
        except Exception as e:
            raise ValueError(f"加载武器数据文件失败: {e}")
    
    def get_weapon(self, weapon_id):
        """根据武器编号获取武器对象"""
        return self.weapons.get(weapon_id)
    
    def get_all_weapons(self):
        """获取所有武器"""
        return list(self.weapons.values())
    
    def add_weapon(self, weapon):
        """添加武器到数据库（不保存到文件）"""
        self.weapons[weapon.weapon_id] = weapon
    
    def save_to_csv(self, file_path=None):
        """将当前武器数据保存到CSV文件"""
        if file_path is None:
            file_path = self.csv_file_path
        
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                fieldnames = ['weapon_id', 'name', 'damage_type_count', 'damage_bonus', 'attribute_modifiers']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                
                for weapon in self.weapons.values():
                    # 将数组转换为字符串
                    damage_bonus_str = ",".join(str(x) for x in weapon.damage_bonus)
                    
                    # 将矩阵转换为字符串
                    modifier_rows = []
                    for row in weapon.attribute_modifiers:
                        modifier_rows.append(",".join(str(x) for x in row))
                    attribute_modifiers_str = ";".join(modifier_rows)
                    
                    writer.writerow({
                        'weapon_id': weapon.weapon_id,
                        'name': weapon.name,
                        'damage_type_count': len(weapon.damage_bonus),
                        'damage_bonus': damage_bonus_str,
                        'attribute_modifiers': attribute_modifiers_str
                    })
                    
        except Exception as e:
            raise ValueError(f"保存武器数据到文件失败: {e}")   
        
        
        
import csv
import os

class State:
    """简化特殊状态类，移除attribute_modifiers，专注于攻击和防御修正"""
    
    def __init__(self, state_id, name, duration, is_positive, description, 
                 # 基础属性修正
                 hp_mod=0, hp_percent_mod=0,
                 stamina_mod=0, stamina_percent_mod=0,
                 holy_light_mod=0, holy_light_percent_mod=0,
                 mana_mod=0, mana_percent_mod=0,
                 
                 # 战斗属性修正
                 initiative_mod=0, movement_mod=0, 
                 dodge_mod=0, crit_mod=0,
                 
                 # 物理攻击修正（细分）
                 physical_attack_pierce_mod=0,  # 穿刺攻击修正
                 physical_attack_slash_mod=0,   # 挥砍攻击修正
                 physical_attack_blunt_mod=0,   # 钝器攻击修正
                 
                 # 魔法攻击修正（细分）
                 magical_attack_arcane_mod=0,   # 奥术攻击修正
                 magical_attack_holy_mod=0,    # 神圣攻击修正
                 magical_attack_water_mod=0,    # 水元素攻击修正
                 magical_attack_fire_mod=0,     # 火元素攻击修正
                 magical_attack_earth_mod=0,    # 土元素攻击修正
                 magical_attack_air_mod=0,      # 气元素攻击修正
                 magical_attack_nature_mod=0,   # 自然攻击修正
                 magical_attack_shadow_mod=0,   # 暗影攻击修正
                 magical_attack_void_mod=0,     # 虚空攻击修正
                 
                 # 物理防御修正（细分）
                 physical_defense_pierce_mod=0,  # 穿刺防御修正
                 physical_defense_slash_mod=0,   # 挥砍防御修正
                 physical_defense_blunt_mod=0,  # 钝器防御修正
                 
                 # 魔法防御修正（细分）
                 magical_defense_arcane_mod=0,   # 奥术防御修正
                 magical_defense_holy_mod=0,    # 神圣防御修正
                 magical_defense_water_mod=0,   # 水元素防御修正
                 magical_defense_fire_mod=0,    # 火元素防御修正
                 magical_defense_earth_mod=0,   # 土元素防御修正
                 magical_defense_air_mod=0,     # 气元素防御修正
                 magical_defense_nature_mod=0,  # 自然防御修正
                 magical_defense_shadow_mod=0):  # 暗影防御修正
        """
        初始化简化特殊状态
        
        Args:
            state_id (int): 状态ID
            name (str): 状态名称
            duration (int): 持续时间（回合数）
            is_positive (bool): 是否为正面状态
            description (str): 状态描述
            各种修正参数...
        """
        self.state_id = state_id
        self.name = name
        self.duration = duration
        self.is_positive = bool(is_positive)
        self.description = description
        
        # 基础属性修正
        self.hp_mod = hp_mod
        self.hp_percent_mod = hp_percent_mod
        self.stamina_mod = stamina_mod
        self.stamina_percent_mod = stamina_percent_mod
        self.holy_light_mod = holy_light_mod
        self.holy_light_percent_mod = holy_light_percent_mod
        self.mana_mod = mana_mod
        self.mana_percent_mod = mana_percent_mod
        
        # 战斗属性修正
        self.initiative_mod = initiative_mod
        self.movement_mod = movement_mod
        self.dodge_mod = dodge_mod
        self.crit_mod = crit_mod
        
        # 物理攻击修正（细分）
        self.physical_attack_pierce_mod = physical_attack_pierce_mod
        self.physical_attack_slash_mod = physical_attack_slash_mod
        self.physical_attack_blunt_mod = physical_attack_blunt_mod
        
        # 魔法攻击修正（细分）
        self.magical_attack_arcane_mod = magical_attack_arcane_mod
        self.magical_attack_holy_mod = magical_attack_holy_mod
        self.magical_attack_water_mod = magical_attack_water_mod
        self.magical_attack_fire_mod = magical_attack_fire_mod
        self.magical_attack_earth_mod = magical_attack_earth_mod
        self.magical_attack_air_mod = magical_attack_air_mod
        self.magical_attack_nature_mod = magical_attack_nature_mod
        self.magical_attack_shadow_mod = magical_attack_shadow_mod
        self.magical_attack_void_mod = magical_attack_void_mod
        
        # 物理防御修正（细分）
        self.physical_defense_pierce_mod = physical_defense_pierce_mod
        self.physical_defense_slash_mod = physical_defense_slash_mod
        self.physical_defense_blunt_mod = physical_defense_blunt_mod
        
        # 魔法防御修正（细分）
        self.magical_defense_arcane_mod = magical_defense_arcane_mod
        self.magical_defense_holy_mod = magical_defense_holy_mod
        self.magical_defense_water_mod = magical_defense_water_mod
        self.magical_defense_fire_mod = magical_defense_fire_mod
        self.magical_defense_earth_mod = magical_defense_earth_mod
        self.magical_defense_air_mod = magical_defense_air_mod
        self.magical_defense_nature_mod = magical_defense_nature_mod
        self.magical_defense_shadow_mod = magical_defense_shadow_mod
    
    def apply_to_unit(self, unit):
        """
        将状态效果应用到单位
        
        Args:
            unit: 要应用状态的单位对象
        """
        # 应用基础属性修正
        if self.hp_mod != 0:
            unit.hp += self.hp_mod
            unit.hp = max(0, min(unit.max_hp, unit.hp))  # 确保在合理范围内
        
        if self.hp_percent_mod != 0:
            unit.hp += unit.max_hp * self.hp_percent_mod
            unit.hp = max(0, min(unit.max_hp, unit.hp))
        
        if self.stamina_mod != 0:
            unit.stamina += self.stamina_mod
            unit.stamina = max(0, min(unit.max_stamina, unit.stamina))
        
        if self.stamina_percent_mod != 0:
            unit.stamina += unit.max_stamina * self.stamina_percent_mod
            unit.stamina = max(0, min(unit.max_stamina, unit.stamina))
        
        if self.holy_light_mod != 0:
            unit.holy_light += self.holy_light_mod
            unit.holy_light = max(0, min(unit.max_holy_light, unit.holy_light))
        
        if self.holy_light_percent_mod != 0:
            unit.holy_light += unit.max_holy_light * self.holy_light_percent_mod
            unit.holy_light = max(0, min(unit.max_holy_light, unit.holy_light))
        
        if self.mana_mod != 0:
            unit.mana += self.mana_mod
            unit.mana = max(0, min(unit.max_mana, unit.mana))
        
        if self.mana_percent_mod != 0:
            unit.mana += unit.max_mana * self.mana_percent_mod
            unit.mana = max(0, min(unit.max_mana, unit.mana))
        
        # 应用战斗属性修正
        unit.initiative += self.initiative_mod
        unit.movement += self.movement_mod
        unit.dodge_rate += self.dodge_mod
        unit.crit_rate += self.crit_mod
    
    def get_physical_attack_modifier(self, attack_type):
        """获取物理攻击力修正"""
        if attack_type == "pierce":
            return self.physical_attack_pierce_mod
        elif attack_type == "slash":
            return self.physical_attack_slash_mod
        elif attack_type == "blunt":
            return self.physical_attack_blunt_mod
        else:
            return 0
    
    def get_magical_attack_modifier(self, magic_type):
        """获取魔法攻击力修正"""
        if magic_type == "arcane":
            return self.magical_attack_arcane_mod
        elif magic_type == "holy":
            return self.magical_attack_holy_mod
        elif magic_type == "water":
            return self.magical_attack_water_mod
        elif magic_type == "fire":
            return self.magical_attack_fire_mod
        elif magic_type == "earth":
            return self.magical_attack_earth_mod
        elif magic_type == "air":
            return self.magical_attack_air_mod
        elif magic_type == "nature":
            return self.magical_attack_nature_mod
        elif magic_type == "shadow":
            return self.magical_attack_shadow_mod
        elif magic_type == "void":
            return self.magical_attack_void_mod
        else:
            return 0
    
    def get_physical_defense_modifier(self, defense_type):
        """获取物理防御修正"""
        if defense_type == "pierce":
            return self.physical_defense_pierce_mod
        elif defense_type == "slash":
            return self.physical_defense_slash_mod
        elif defense_type == "blunt":
            return self.physical_defense_blunt_mod
        else:
            return 0
    
    def get_magical_defense_modifier(self, defense_type):
        """获取魔法防御修正"""
        if defense_type == "arcane":
            return self.magical_defense_arcane_mod
        elif defense_type == "holy":
            return self.magical_defense_holy_mod
        elif defense_type == "water":
            return self.magical_defense_water_mod
        elif defense_type == "fire":
            return self.magical_defense_fire_mod
        elif defense_type == "earth":
            return self.magical_defense_earth_mod
        elif defense_type == "air":
            return self.magical_defense_air_mod
        elif defense_type == "nature":
            return self.magical_defense_nature_mod
        elif defense_type == "shadow":
            return self.magical_defense_shadow_mod
        else:
            return 0
    
    def __str__(self):
        return f"SimplifiedState[{self.state_id}]: {self.name} ({self.duration}回合) - {self.description}"

class StateDatabase:
    """简化特殊状态数据库，从CSV文件加载状态数据"""
    
    def __init__(self, csv_file_path="states_simplified.csv"):
        self.states = {}  # state_id -> SimplifiedState对象
        self.csv_file_path = csv_file_path
        self._load_from_csv()
    
    def _load_from_csv(self):
        """从CSV文件加载简化状态数据"""
        if not os.path.exists(self.csv_file_path):
            raise FileNotFoundError(f"状态数据文件不存在: {self.csv_file_path}")
        
        try:
            with open(self.csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row_num, row in enumerate(reader, start=2):  # 从第2行开始（跳过标题）
                    try:
                       
                        # 解析基本字段
                        state_id = int(row['state_id'])
                        name = row['name']
                        duration = int(row['duration'])
                        is_positive = int(row['is_positive'])
                        description = row['description']
                        
                        # 解析数值修正字段
                        hp_mod = float(row.get('hp_mod', 0))
                        hp_percent_mod = float(row.get('hp_percent_mod', 0))
                        stamina_mod = float(row.get('stamina_mod', 0))
                        stamina_percent_mod = float(row.get('stamina_percent_mod', 0))
                        holy_light_mod = float(row.get('holy_light_mod', 0))
                        holy_light_percent_mod = float(row.get('holy_light_percent_mod', 0))
                        mana_mod = float(row.get('mana_mod', 0))
                        mana_percent_mod = float(row.get('mana_percent_mod', 0))
                        
                        initiative_mod = float(row.get('initiative_mod', 0))
                        movement_mod = float(row.get('movement_mod', 0))
                        dodge_mod = float(row.get('dodge_mod', 0))
                        crit_mod = float(row.get('crit_mod', 0))
                        
                        # 解析物理攻击修正（细分）
                        physical_attack_pierce_mod = float(row.get('physical_attack_pierce_mod', 0))
                        physical_attack_slash_mod = float(row.get('physical_attack_slash_mod', 0))
                        physical_attack_blunt_mod = float(row.get('physical_attack_blunt_mod', 0))
                        
                        # 解析魔法攻击修正（细分）
                        magical_attack_arcane_mod = float(row.get('magical_attack_arcane_mod', 0))
                        magical_attack_holy_mod = float(row.get('magical_attack_holy_mod', 0))
                        magical_attack_water_mod = float(row.get('magical_attack_water_mod', 0))
                        magical_attack_fire_mod = float(row.get('magical_attack_fire_mod', 0))
                        magical_attack_earth_mod = float(row.get('magical_attack_earth_mod', 0))
                        magical_attack_air_mod = float(row.get('magical_attack_air_mod', 0))
                        magical_attack_nature_mod = float(row.get('magical_attack_nature_mod', 0))
                        magical_attack_shadow_mod = float(row.get('magical_attack_shadow_mod', 0))
                        magical_attack_void_mod = float(row.get('magical_attack_void_mod', 0))
                        
                        # 解析物理防御修正（细分）
                        physical_defense_pierce_mod = float(row.get('physical_defense_pierce_mod', 0))
                        physical_defense_slash_mod = float(row.get('physical_defense_slash_mod', 0))
                        physical_defense_blunt_mod = float(row.get('physical_defense_blunt_mod', 0))
                        
                        # 解析魔法防御修正（细分）
                        magical_defense_arcane_mod = float(row.get('magical_defense_arcane_mod', 0))
                        magical_defense_holy_mod = float(row.get('magical_defense_holy_mod', 0))
                        magical_defense_water_mod = float(row.get('magical_defense_water_mod', 0))
                        magical_defense_fire_mod = float(row.get('magical_defense_fire_mod', 0))
                        magical_defense_earth_mod = float(row.get('magical_defense_earth_mod', 0))
                        magical_defense_air_mod = float(row.get('magical_defense_air_mod', 0))
                        magical_defense_nature_mod = float(row.get('magical_defense_nature_mod', 0))
                        magical_defense_shadow_mod = float(row.get('magical_defense_shadow_mod', 0))
                        
                        # 创建简化状态对象（不再包含attribute_modifiers）
                        state = State(
                            state_id, name, duration, is_positive, description,
                            hp_mod, hp_percent_mod,
                            stamina_mod, stamina_percent_mod,
                            holy_light_mod, holy_light_percent_mod,
                            mana_mod, mana_percent_mod,
                            initiative_mod, movement_mod,
                            dodge_mod, crit_mod,
                            physical_attack_pierce_mod, physical_attack_slash_mod, physical_attack_blunt_mod,
                            magical_attack_arcane_mod, magical_attack_holy_mod, magical_attack_water_mod,
                            magical_attack_fire_mod, magical_attack_earth_mod, magical_attack_air_mod,
                            magical_attack_nature_mod, magical_attack_shadow_mod, magical_attack_void_mod,
                            physical_defense_pierce_mod, physical_defense_slash_mod, physical_defense_blunt_mod,
                            magical_defense_arcane_mod, magical_defense_holy_mod, magical_defense_water_mod,
                            magical_defense_fire_mod, magical_defense_earth_mod, magical_defense_air_mod,
                            magical_defense_nature_mod, magical_defense_shadow_mod
                        )
                        
                        self.states[state_id] = state
                        
                    except (KeyError, ValueError) as e:
                        print(f"警告: 解析第{row_num}行数据失败: {e}")
                        continue
                        
        except Exception as e:
            raise ValueError(f"加载简化状态数据文件失败: {e}")
    
    def get_state(self, state_id):
        """根据状态ID获取状态对象"""
        return self.states.get(state_id)
    
    def get_all_states(self):
        """获取所有状态"""
        return list(self.states.values())
    
    def get_states_by_type(self, is_positive=True):
        """根据类型获取状态（正面/负面）"""
        return [state for state in self.states.values() if state.is_positive == is_positive]
    
    def add_state(self, state):
        """添加状态到数据库（不保存到文件）"""
        self.states[state.state_id] = state
    
    def save_to_csv(self, file_path=None):
        """将当前状态数据保存到CSV文件"""
        if file_path is None:
            file_path = self.csv_file_path
        
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                fieldnames = [
                    'state_id', 'name', 'duration', 'is_positive', 'description',
                    'hp_mod', 'hp_percent_mod',
                    'stamina_mod', 'stamina_percent_mod',
                    'holy_light_mod', 'holy_light_percent_mod',
                    'mana_mod', 'mana_percent_mod',
                    'initiative_mod', 'movement_mod',
                    'dodge_mod', 'crit_mod',
                    'physical_attack_pierce_mod', 'physical_attack_slash_mod', 'physical_attack_blunt_mod',
                    'magical_attack_arcane_mod', 'magical_attack_holy_mod', 'magical_attack_water_mod',
                    'magical_attack_fire_mod', 'magical_attack_earth_mod', 'magical_attack_air_mod',
                    'magical_attack_nature_mod', 'magical_attack_shadow_mod', 'magical_attack_void_mod',
                    'physical_defense_pierce_mod', 'physical_defense_slash_mod', 'physical_defense_blunt_mod',
                    'magical_defense_arcane_mod', 'magical_defense_holy_mod', 'magical_defense_water_mod',
                    'magical_defense_fire_mod', 'magical_defense_earth_mod', 'magical_defense_air_mod',
                    'magical_defense_nature_mod', 'magical_defense_shadow_mod'
                ]
                
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                for state in self.states.values():
                    writer.writerow({
                        'state_id': state.state_id,
                        'name': state.name,
                        'duration': state.duration,
                        'is_positive': 1 if state.is_positive else 0,
                        'description': state.description,
                        'hp_mod': state.hp_mod,
                        'hp_percent_mod': state.hp_percent_mod,
                        'stamina_mod': state.stamina_mod,
                        'stamina_percent_mod': state.stamina_percent_mod,
                        'holy_light_mod': state.holy_light_mod,
                        'holy_light_percent_mod': state.holy_light_percent_mod,
                        'mana_mod': state.mana_mod,
                        'mana_percent_mod': state.mana_percent_mod,
                        'initiative_mod': state.initiative_mod,
                        'movement_mod': state.movement_mod,
                        'dodge_mod': state.dodge_mod,
                        'crit_mod': state.crit_mod,
                        'physical_attack_pierce_mod': state.physical_attack_pierce_mod,
                        'physical_attack_slash_mod': state.physical_attack_slash_mod,
                        'physical_attack_blunt_mod': state.physical_attack_blunt_mod,
                        'magical_attack_arcane_mod': state.magical_attack_arcane_mod,
                        'magical_attack_holy_mod': state.magical_attack_holy_mod,
                        'magical_attack_water_mod': state.magical_attack_water_mod,
                        'magical_attack_fire_mod': state.magical_attack_fire_mod,
                        'magical_attack_earth_mod': state.magical_attack_earth_mod,
                        'magical_attack_air_mod': state.magical_attack_air_mod,
                        'magical_attack_nature_mod': state.magical_attack_nature_mod,
                        'magical_attack_shadow_mod': state.magical_attack_shadow_mod,
                        'magical_attack_void_mod': state.magical_attack_void_mod,
                        'physical_defense_pierce_mod': state.physical_defense_pierce_mod,
                        'physical_defense_slash_mod': state.physical_defense_slash_mod,
                        'physical_defense_blunt_mod': state.physical_defense_blunt_mod,
                        'magical_defense_arcane_mod': state.magical_defense_arcane_mod,
                        'magical_defense_holy_mod': state.magical_defense_holy_mod,
                        'magical_defense_water_mod': state.magical_defense_water_mod,
                        'magical_defense_fire_mod': state.magical_defense_fire_mod,
                        'magical_defense_earth_mod': state.magical_defense_earth_mod,
                        'magical_defense_air_mod': state.magical_defense_air_mod,
                        'magical_defense_nature_mod': state.magical_defense_nature_mod,
                        'magical_defense_shadow_mod': state.magical_defense_shadow_mod
                    })
                    
        except Exception as e:
            raise ValueError(f"保存简化状态数据到文件失败: {e}")

import csv
import os

class Monster:
    """魔物类，包含魔物的属性和能力"""
    
    def __init__(self, monster_id, name, size, description, skills,
                 # 基础属性
                 hp, stamina, mana,
                 initiative, movement, dodge_rate, crit_rate,
                 
                 # 物理攻击属性
                 physical_attack_pierce, physical_attack_slash, physical_attack_blunt,
                 
                 # 魔法攻击属性
                 magical_attack_arcane, magical_attack_holy, magical_attack_water,
                 magical_attack_fire, magical_attack_earth, magical_attack_air,
                 magical_attack_nature, magical_attack_shadow, magical_attack_void,
                 
                 # 物理防御属性
                 physical_defense_pierce, physical_defense_slash, physical_defense_blunt,
                 
                 # 魔法防御属性
                 magical_defense_arcane, magical_defense_holy, magical_defense_water,
                 magical_defense_fire, magical_defense_earth, magical_defense_air,
                 magical_defense_nature, magical_defense_shadow,
                 
                 # 特殊能力
                 has_void_gland=False, void_fog_damage=0, void_fog_range=0):
        """
        初始化魔物
        
        Args:
            monster_id (int): 魔物ID
            name (str): 魔物名称
            size (str): 体型（small/medium/large/giant）
            description (str): 魔物描述
            skills (str): 技能代号列表字符串（分号分隔）
            各种属性参数...
        """
        self.monster_id = monster_id
        self.name = name
        self.size = size
        self.description = description
        
        # 解析技能列表
        if skills:
            self.skill_ids = [int(skill_id.strip()) for skill_id in skills.split(";") if skill_id.strip()]
        else:
            self.skill_ids = []
        
        # 基础属性
        self.max_hp = hp
        self.hp = hp
        self.max_stamina = stamina
        self.stamina = stamina
        self.max_mana = mana
        self.mana = mana
        
        # 战斗属性
        self.initiative = initiative
        self.movement = movement
        self.dodge_rate = dodge_rate
        self.crit_rate = crit_rate
        
        # 物理攻击属性
        self.physical_attack_pierce = physical_attack_pierce
        self.physical_attack_slash = physical_attack_slash
        self.physical_attack_blunt = physical_attack_blunt
        
        # 魔法攻击属性
        self.magical_attack_arcane = magical_attack_arcane
        self.magical_attack_holy = magical_attack_holy
        self.magical_attack_water = magical_attack_water
        self.magical_attack_fire = magical_attack_fire
        self.magical_attack_earth = magical_attack_earth
        self.magical_attack_air = magical_attack_air
        self.magical_attack_nature = magical_attack_nature
        self.magical_attack_shadow = magical_attack_shadow
        self.magical_attack_void = magical_attack_void
        
        # 物理防御属性
        self.physical_defense_pierce = physical_defense_pierce
        self.physical_defense_slash = physical_defense_slash
        self.physical_defense_blunt = physical_defense_blunt
        
        # 魔法防御属性
        self.magical_defense_arcane = magical_defense_arcane
        self.magical_defense_holy = magical_defense_holy
        self.magical_defense_water = magical_defense_water
        self.magical_defense_fire = magical_defense_fire
        self.magical_defense_earth = magical_defense_earth
        self.magical_defense_air = magical_defense_air
        self.magical_defense_nature = magical_defense_nature
        self.magical_defense_shadow = magical_defense_shadow
        
        # 虚空相关属性
        self.has_void_gland = bool(has_void_gland)
        self.void_fog_damage = void_fog_damage
        self.void_fog_range = void_fog_range
        self.void_fog_active = self.has_void_gland
        self.void_gland_destroyed = False
        self.void_recovery_timer = 0
        
        # 恐惧力场（根据体型计算）
        self.fear_strength, self.fear_range = self._calculate_fear_field()
    
    def _calculate_fear_field(self):
        """根据体型计算恐惧力场强度和范围"""
        size_to_fear = {
            'small': (1, 1),      # 强度1，范围1
            'medium': (2, 5),     # 强度2，范围5
            'large': (3, 10),     # 强度3，范围10
            'giant': (4, 25)      # 强度4，范围25
        }
        return size_to_fear.get(self.size, (0, 0))
    
    def get_physical_attack(self, attack_type):
        """获取物理攻击力"""
        if attack_type == "pierce":
            return self.physical_attack_pierce
        elif attack_type == "slash":
            return self.physical_attack_slash
        elif attack_type == "blunt":
            return self.physical_attack_blunt
        else:
            return 0
    
    def get_magical_attack(self, magic_type):
        """获取魔法攻击力"""
        if magic_type == "arcane":
            return self.magical_attack_arcane
        elif magic_type == "holy":
            return self.magical_attack_holy
        elif magic_type == "water":
            return self.magical_attack_water
        elif magic_type == "fire":
            return self.magical_attack_fire
        elif magic_type == "earth":
            return self.magical_attack_earth
        elif magic_type == "air":
            return self.magical_attack_air
        elif magic_type == "nature":
            return self.magical_attack_nature
        elif magic_type == "shadow":
            return self.magical_attack_shadow
        elif magic_type == "void":
            return self.magical_attack_void
        else:
            return 0
    
    def get_physical_defense(self, defense_type):
        """获取物理防御力"""
        if defense_type == "pierce":
            return self.physical_defense_pierce
        elif defense_type == "slash":
            return self.physical_defense_slash
        elif defense_type == "blunt":
            return self.physical_defense_blunt
        else:
            return 0
    
    def get_magical_defense(self, defense_type):
        """获取魔法防御力"""
        if defense_type == "arcane":
            return self.magical_defense_arcane
        elif defense_type == "holy":
            return self.magical_defense_holy
        elif defense_type == "water":
            return self.magical_defense_water
        elif defense_type == "fire":
            return self.magical_defense_fire
        elif defense_type == "earth":
            return self.magical_defense_earth
        elif defense_type == "air":
            return self.magical_defense_air
        elif defense_type == "nature":
            return self.magical_defense_nature
        elif defense_type == "shadow":
            return self.magical_defense_shadow
        else:
            return 0
    
    def apply_fear_effect(self, intelligent_units, distance_calculator):
        """
        应用恐惧力场效果
        
        Args:
            intelligent_units: 智能单位列表
            distance_calculator: 距离计算函数
        """
        for unit in intelligent_units:
            # 检查单位是否在恐惧力场范围内
            distance = distance_calculator(self.position, unit.position)
            if distance <= self.fear_range:
                # 检查单位的圣光护盾等级是否足够抵抗恐惧
                if hasattr(unit, 'holy_shield_level') and unit.holy_shield_level < self.fear_strength:
                    unit.skip_turn = True  # 单位跳过本回合
    
    def apply_void_fog(self, units, distance_calculator):
        """
        应用虚空雾效果（如果有虚空腺体且未被破坏）
        
        Args:
            units: 单位列表
            distance_calculator: 距离计算函数
        """
        if not self.has_void_gland or self.void_gland_destroyed or not self.void_fog_active:
            return
        
        for unit in units:
            distance = distance_calculator(self.position, unit.position)
            if distance <= self.void_fog_range:
                # 对单位造成虚空伤害
                unit.take_damage(self.void_fog_damage, 'magical', 'void')
    
    def destroy_void_gland(self):
        """破坏虚空腺体"""
        if self.has_void_gland and not self.void_gland_destroyed:
            self.void_gland_destroyed = True
            self.void_fog_active = False
            self.void_recovery_timer = 3  # 3回合后恢复
    
    def update_void_gland(self):
        """更新虚空腺体状态（每回合调用）"""
        if self.void_gland_destroyed and self.void_recovery_timer > 0:
            self.void_recovery_timer -= 1
            if self.void_recovery_timer <= 0:
                # 恢复虚空腺体
                self.void_gland_destroyed = False
                self.void_fog_active = True
    
    def take_damage(self, damage, damage_type, attack_type):
        """
        魔物承受伤害
        
        Args:
            damage: 伤害值
            damage_type: 伤害类型（physical/magical）
            attack_type: 攻击类型（pierce/slash/blunt/arcane等）
        """
        # 计算实际伤害（考虑防御）
        if damage_type == "physical":
            defense = self.get_physical_defense(attack_type)
        else:  # magical
            defense = self.get_magical_defense(attack_type)
        
        # 计算减伤（防御值转换为减伤百分比，最高90%）
        damage_reduction = min(0.9, defense / (defense + 100))
        actual_damage = damage * (1 - damage_reduction)
        
        self.hp -= actual_damage
        
        # 检查是否死亡
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
        
        return actual_damage
    
    def use_skill(self, skill_id, target=None):
        """
        使用技能
        
        Args:
            skill_id: 技能ID
            target: 技能目标（可选）
        """
        if skill_id not in self.skill_ids:
            return False, "魔物不会此技能"
        
        # 这里可以添加技能的具体实现
        # 根据技能ID执行不同的技能效果
        
        return True, f"{self.name}使用了技能{skill_id}"
    
    def recover_resources(self):
        """恢复资源（每回合调用）"""
        # 恢复体力（基础恢复率为最大体力的10%）
        stamina_recovery = self.max_stamina * 0.1
        self.stamina = min(self.max_stamina, self.stamina + stamina_recovery)
        
        # 恢复魔力（基础恢复率为最大魔力的10%）
        mana_recovery = self.max_mana * 0.1
        self.mana = min(self.max_mana, self.mana + mana_recovery)
    
    def __str__(self):
        return f"Monster[{self.monster_id}]: {self.name} ({self.size}) - HP: {self.hp}/{self.max_hp}"

class MonsterDatabase:
    """魔物数据库，从CSV文件加载魔物数据"""
    
    def __init__(self, csv_file_path="monsters.csv"):
        self.monsters = {}  # monster_id -> Monster对象
        self.csv_file_path = csv_file_path
        self._load_from_csv()
    
    def _load_from_csv(self):
        """从CSV文件加载魔物数据"""
        if not os.path.exists(self.csv_file_path):
            raise FileNotFoundError(f"魔物数据文件不存在: {self.csv_file_path}")
        
        try:
            with open(self.csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row_num, row in enumerate(reader, start=2):  # 从第2行开始（跳过标题）
                    try:
                        # 解析基本字段
                        monster_id = int(row['monster_id'])
                        name = row['name']
                        size = row['size']
                        description = row['description']
                        skills = row['skills']
                        
                        # 解析基础属性
                        hp = float(row['hp'])
                        stamina = float(row['stamina'])
                        mana = float(row['mana'])
                        
                        initiative = float(row['initiative'])
                        movement = float(row['movement'])
                        dodge_rate = float(row['dodge_rate'])
                        crit_rate = float(row['crit_rate'])
                        
                        # 解析物理攻击属性
                        physical_attack_pierce = float(row['physical_attack_pierce'])
                        physical_attack_slash = float(row['physical_attack_slash'])
                        physical_attack_blunt = float(row['physical_attack_blunt'])
                        
                        # 解析魔法攻击属性
                        magical_attack_arcane = float(row['magical_attack_arcane'])
                        magical_attack_holy = float(row['magical_attack_holy'])
                        magical_attack_water = float(row['magical_attack_water'])
                        magical_attack_fire = float(row['magical_attack_fire'])
                        magical_attack_earth = float(row['magical_attack_earth'])
                        magical_attack_air = float(row['magical_attack_air'])
                        magical_attack_nature = float(row['magical_attack_nature'])
                        magical_attack_shadow = float(row['magical_attack_shadow'])
                        magical_attack_void = float(row['magical_attack_void'])
                        
                        # 解析物理防御属性
                        physical_defense_pierce = float(row['physical_defense_pierce'])
                        physical_defense_slash = float(row['physical_defense_slash'])
                        physical_defense_blunt = float(row['physical_defense_blunt'])
                        
                        # 解析魔法防御属性
                        magical_defense_arcane = float(row['magical_defense_arcane'])
                        magical_defense_holy = float(row['magical_defense_holy'])
                        magical_defense_water = float(row['magical_defense_water'])
                        magical_defense_fire = float(row['magical_defense_fire'])
                        magical_defense_earth = float(row['magical_defense_earth'])
                        magical_defense_air = float(row['magical_defense_air'])
                        magical_defense_nature = float(row['magical_defense_nature'])
                        magical_defense_shadow = float(row['magical_defense_shadow'])
                        
                        # 解析特殊能力
                        has_void_gland = int(row.get('has_void_gland', 0))
                        void_fog_damage = float(row.get('void_fog_damage', 0))
                        void_fog_range = float(row.get('void_fog_range', 0))
                        
                        # 创建魔物对象
                        monster = Monster(
                            monster_id, name, size, description, skills,
                            hp, stamina, mana,
                            initiative, movement, dodge_rate, crit_rate,
                            physical_attack_pierce, physical_attack_slash, physical_attack_blunt,
                            magical_attack_arcane, magical_attack_holy, magical_attack_water,
                            magical_attack_fire, magical_attack_earth, magical_attack_air,
                            magical_attack_nature, magical_attack_shadow, magical_attack_void,
                            physical_defense_pierce, physical_defense_slash, physical_defense_blunt,
                            magical_defense_arcane, magical_defense_holy, magical_defense_water,
                            magical_defense_fire, magical_defense_earth, magical_defense_air,
                            magical_defense_nature, magical_defense_shadow,
                            has_void_gland, void_fog_damage, void_fog_range
                        )
                        
                        self.monsters[monster_id] = monster
                        
                    except (KeyError, ValueError) as e:
                        print(f"警告: 解析第{row_num}行数据失败: {e}")
                        continue
                        
        except Exception as e:
            raise ValueError(f"加载魔物数据文件失败: {e}")
    
    def get_monster(self, monster_id):
        """根据魔物ID获取魔物对象"""
        return self.monsters.get(monster_id)
    
    def get_all_monsters(self):
        """获取所有魔物"""
        return list(self.monsters.values())
    
    def get_monsters_by_size(self, size):
        """根据体型获取魔物"""
        return [monster for monster in self.monsters.values() if monster.size == size]
    
    def add_monster(self, monster):
        """添加魔物到数据库"""
        self.monsters[monster.monster_id] = monster
    
    def save_to_csv(self, file_path=None):
        """将当前魔物数据保存到CSV文件"""
        if file_path is None:
            file_path = self.csv_file_path
        
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                fieldnames = [
                    'monster_id', 'name', 'size', 'description', 'skills',
                    'hp', 'stamina', 'mana',
                    'initiative', 'movement', 'dodge_rate', 'crit_rate',
                    'physical_attack_pierce', 'physical_attack_slash', 'physical_attack_blunt',
                    'magical_attack_arcane', 'magical_attack_holy', 'magical_attack_water',
                    'magical_attack_fire', 'magical_attack_earth', 'magical_attack_air',
                    'magical_attack_nature', 'magical_attack_shadow', 'magical_attack_void',
                    'physical_defense_pierce', 'physical_defense_slash', 'physical_defense_blunt',
                    'magical_defense_arcane', 'magical_defense_holy', 'magical_defense_water',
                    'magical_defense_fire', 'magical_defense_earth', 'magical_defense_air',
                    'magical_defense_nature', 'magical_defense_shadow',
                    'has_void_gland', 'void_fog_damage', 'void_fog_range'
                ]
                
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                for monster in self.monsters.values():
                    # 将技能列表转换为字符串
                    skills_str = ";".join(str(skill_id) for skill_id in monster.skill_ids)
                    
                    writer.writerow({
                        'monster_id': monster.monster_id,
                        'name': monster.name,
                        'size': monster.size,
                        'description': monster.description,
                        'skills': skills_str,
                        'hp': monster.max_hp,
                        'stamina': monster.max_stamina,
                        'mana': monster.max_mana,
                        'initiative': monster.initiative,
                        'movement': monster.movement,
                        'dodge_rate': monster.dodge_rate,
                        'crit_rate': monster.crit_rate,
                        'physical_attack_pierce': monster.physical_attack_pierce,
                        'physical_attack_slash': monster.physical_attack_slash,
                        'physical_attack_blunt': monster.physical_attack_blunt,
                        'magical_attack_arcane': monster.magical_attack_arcane,
                        'magical_attack_holy': monster.magical_attack_holy,
                        'magical_attack_water': monster.magical_attack_water,
                        'magical_attack_fire': monster.magical_attack_fire,
                        'magical_attack_earth': monster.magical_attack_earth,
                        'magical_attack_air': monster.magical_attack_air,
                        'magical_attack_nature': monster.magical_attack_nature,
                        'magical_attack_shadow': monster.magical_attack_shadow,
                        'magical_attack_void': monster.magical_attack_void,
                        'physical_defense_pierce': monster.physical_defense_pierce,
                        'physical_defense_slash': monster.physical_defense_slash,
                        'physical_defense_blunt': monster.physical_defense_blunt,
                        'magical_defense_arcane': monster.magical_defense_arcane,
                        'magical_defense_holy': monster.magical_defense_holy,
                        'magical_defense_water': monster.magical_defense_water,
                        'magical_defense_fire': monster.magical_defense_fire,
                        'magical_defense_earth': monster.magical_defense_earth,
                        'magical_defense_air': monster.magical_defense_air,
                        'magical_defense_nature': monster.magical_defense_nature,
                        'magical_defense_shadow': monster.magical_defense_shadow,
                        'has_void_gland': 1 if monster.has_void_gland else 0,
                        'void_fog_damage': monster.void_fog_damage,
                        'void_fog_range': monster.void_fog_range
                    })
                    
        except Exception as e:
            raise ValueError(f"保存魔物数据到文件失败: {e}")

