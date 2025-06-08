import os
import json
import shutil
from datetime import datetime
from openpyxl import Workbook
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class DataManager:
    """数据管理器类，负责项目文件的创建、保存和加载"""
    
    def __init__(self):
        self.current_project_path = None
        self.project_data = {}
        self.indicator_data = {}
    
    def create_new_project(self, parent_widget=None):
        """创建新项目"""
        # 选择项目保存位置
        folder_path = QFileDialog.getExistingDirectory(
            parent_widget,
            "选择项目保存位置",
            os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        
        if not folder_path:
            return None
        
        # 生成项目文件夹名称
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        project_name = f"新项目_{timestamp}"
        project_path = os.path.join(folder_path, project_name)
        
        try:
            # 创建项目文件夹
            os.makedirs(project_path, exist_ok=True)
            
            # 创建输出表格子文件夹
            output_folder = os.path.join(project_path, "输出表格")
            os.makedirs(output_folder, exist_ok=True)
            
            # 创建JSON文件
            self.create_json_files(project_path)
            
            # 创建Excel文件
            self.create_excel_files(project_path)
            
            # 创建输出表格
            self.create_output_excel_files(output_folder)
            
            self.current_project_path = project_path
            
            return project_path
            
        except Exception as e:
            if parent_widget:
                QMessageBox.critical(parent_widget, "错误", f"创建项目失败：{str(e)}")
            return None
    
    def create_json_files(self, project_path):
        """创建JSON文件"""
        # 创建 User_input.json
        user_input_data = self.get_default_user_input_data()
        with open(os.path.join(project_path, "User_input.json"), 'w', encoding='utf-8') as f:
            json.dump(user_input_data, f, ensure_ascii=False, indent=2)
        
        # 创建 IndicatorSystem.json
        indicator_system_data = self.get_default_indicator_system_data()
        with open(os.path.join(project_path, "IndicatorSystem.json"), 'w', encoding='utf-8') as f:
            json.dump(indicator_system_data, f, ensure_ascii=False, indent=2)
    
    def create_excel_files(self, project_path):
        """创建Excel文件"""
        excel_files = [
            "ESS-电储能装置充放功率(kW·h).xlsx",
            "HES-氢储能装置加氢放氢(kg).xlsx",
            "PV-光伏机组出力(kW).xlsx",
            "WT-风力发电单元出力(kW).xlsx",
            "外部能源网-系统与外部氢源的交互质量(kg).xlsx",
            "外部能源网-系统与外部电网的交互功率(kW).xlsx",
            "氢负荷-合成氨所耗氢气质量(kg).xlsx",
            "氢负荷-氢燃料电池汽车加氢所耗氢气质量(kg).xlsx",
            "氢负荷-生产甲醇所耗氢气质量(kg).xlsx",
            "氢负荷-用于其他方面的销售氢气年总质量(kg).xlsx",
            "氢负荷-用于炼油所耗氢气质量(kg).xlsx",
            "氢负荷-用于钢铁冶炼所耗氢气质量(kg).xlsx",
            "氧负荷-销售氧气的质量(kg).xlsx",
            "电负荷-电负荷所消耗的功率(kW).xlsx"
        ]
        
        for filename in excel_files:
            wb = Workbook()
            ws = wb.active
            ws.title = "数据"
            
            # 不添加任何表头或数据，保持完全空白
            
            # 保存文件
            wb.save(os.path.join(project_path, filename))
    
    def create_output_excel_files(self, output_folder):
        """创建输出表格文件"""
        output_files = [
            "利润表.xlsx",
            "成本费用表.xlsx",
            "现金流量表.xlsx",
            "还本付息表.xlsx"
        ]
        
        for filename in output_files:
            wb = Workbook()
            ws = wb.active
            ws.title = "数据"
            wb.save(os.path.join(output_folder, filename))
    
    def get_default_user_input_data(self):
        """获取默认的用户输入数据"""
        return {
            "项目基本信息": {
                "项目名称": {"单位": "-", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "项目生命周期": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "项目人数": {"单位": "人", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "方案个数": {"单位": "个", "类型": "General", "选择状态": True, "数值": None, "备注": ""}
            },
            "财税与融资参数": {
                "增值税率": {"单位": "%", "类型": "General", "选择状态": True, "数值": 13, "备注": ""},
                "企业所得税率": {"单位": "%", "类型": "General", "选择状态": True, "数值": 25, "备注": ""},
                "增值税附加税率": {"单位": "%", "类型": "General", "选择状态": True, "数值": 3.14, "备注": ""},
                "自有资金比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "贷款利率": {"单位": "%", "类型": "General", "选择状态": True, "数值": 4.9, "备注": ""}
            },
            "财务分析参数": {
                "名义贴现率": {"单位": "%", "类型": "General", "选择状态": True, "数值": 8, "备注": ""},
                "预期通货膨胀率": {"单位": "%", "类型": "General", "选择状态": True, "数值": 2, "备注": ""}
            },
            "价格参数": {
                "氧气的销售价格": {"单位": "元/kg", "类型": "General", "选择状态": True, "数值": [0.5]*24, "备注": ""},
                "电能销售价格": {"单位": "元/kW·h", "类型": "General", "选择状态": True, "数值": [0.3]*24, "备注": ""},
                "电能的购买价格": {"单位": "元/kW·h", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位质量氢能的价格": {"单位": "元/kg", "类型": "General", "选择状态": True, "数值": [33.4]*24, "备注": ""}
            },
            "成本参数": {
                "场地购置费用": {"单位": "万元", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "工程施工费用": {"单位": "万元", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "年人员费用": {"单位": "元/年·人", "类型": "General", "选择状态": True, "数值": None, "备注": ""}
            },
            "WT": {
                "设备选择状态": True,
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "电力电子接口装置成本设备成本的比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量维护成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "风力发电总装机": {"单位": "kW", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "PV": {
                "设备选择状态": True,
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "电力电子接口装置成本设备成本的比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量维护成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "光伏机组总装机": {"单位": "kW", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "EL": {
                "设备选择状态": True,
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "能量转化系数": {"单位": "1", "类型": "General", "选择状态": True, "数值": 33.4, "备注": ""},
                "电力电子接口装置成本设备成本的比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量维护成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "电解槽配置容量": {"单位": "kW", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "HES": {
                "设备选择状态": True,
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量投资成本": {"单位": "元/kg", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量维护成本": {"单位": "元/kg", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "氢储能装置配置容量": {"单位": "kg", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "HFC": {
                "设备选择状态": True,
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "电力电子接口装置成本设备成本的比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量维护成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "燃料电池配置容量": {"单位": "kW", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "ESS": {
                "设备选择状态": True,
                "蓄电池充放电效率": {"单位": "%", "类型": "General", "选择状态": True, "数值": 90, "备注": ""},
                "蓄电池单位运行成本": {"单位": "元/kW·h", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "电力电子接口装置成本设备成本的比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW·h", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "蓄电池配置容量": {"单位": "kW·h", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "外部电网": {"设备选择状态": True},
            "外部氢源": {"设备选择状态": True},
            "氧负荷": {
                "售氧": {"设备选择状态": True}
            },
            "氢负荷": {
                "合成氨": {"设备选择状态": True},
                "合成甲醇": {"设备选择状态": True},
                "成品油加工": {"设备选择状态": True},
                "燃料电池汽车加氢": {"设备选择状态": True},
                "钢铁冶炼": {"设备选择状态": True},
                "其他用途售氢": {"设备选择状态": True}
            },
            "电负荷": {
                "系统内用电单元": {"设备选择状态": True}
            }
        }
    
    def get_default_indicator_system_data(self):
        """获取默认的指标系统数据"""
        return {
            "财务效益指标": {
                "初始投资成本": {
                    "指标编码": "A1", "指标类型": -1, "单位": "万元", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                },
                "年运维成本": {
                    "指标编码": "A2", "指标类型": -1, "单位": "万元", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                },
                "能源外购成本": {
                    "指标编码": "A3", "指标类型": -1, "单位": "万元", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                },
                "净现值": {
                    "指标编码": "A4", "指标类型": 1, "单位": "万元", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                },
                "内部收益率": {
                    "指标编码": "A5", "指标类型": 1, "单位": "%", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                },
                "投资回收期": {
                    "指标编码": "A6", "指标类型": 1, "单位": "年", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                }
            },
            "技术效益指标": {
                "能源网供应占比": {
                    "指标编码": "B1", "指标类型": -1, "单位": "%", "选择状态": False,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                },
                "电储能利用水平": {
                    "指标编码": "B2", "指标类型": 1, "单位": "%", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                },
                "氢储能利用水平": {
                    "指标编码": "B3", "指标类型": 1, "单位": "%", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                },
                "等效可利用小时数": {
                    "指标编码": "B4", "指标类型": 1, "单位": "小时", "选择状态": False,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                }
            },
            "环境效益指标": {
                "可再生能源供应占比": {
                    "指标编码": "C1", "指标类型": 1, "单位": "%", "选择状态": True,
                    "数值": None, "规范化值": None, "综合评估得分分量": None,
                    "critic": None, "demantel": None, "组合权值": None, "备注": ""
                }
            }
        }
    
    def save_project_data(self, project_data, indicator_data):
        """保存项目数据到JSON文件"""
        if not self.current_project_path:
            return False
        
        try:
            # 更新User_input.json
            user_input_path = os.path.join(self.current_project_path, "User_input.json")
            with open(user_input_path, 'r', encoding='utf-8') as f:
                user_input_data = json.load(f)
            
            # 更新数据
            self.update_user_input_data(user_input_data, project_data)
            
            # 保存更新后的数据
            with open(user_input_path, 'w', encoding='utf-8') as f:
                json.dump(user_input_data, f, ensure_ascii=False, indent=2)
            
            # 更新IndicatorSystem.json
            indicator_path = os.path.join(self.current_project_path, "IndicatorSystem.json")
            with open(indicator_path, 'r', encoding='utf-8') as f:
                indicator_system_data = json.load(f)
            
            # 更新指标选择状态
            self.update_indicator_data(indicator_system_data, indicator_data)
            
            # 保存更新后的数据
            with open(indicator_path, 'w', encoding='utf-8') as f:
                json.dump(indicator_system_data, f, ensure_ascii=False, indent=2)
            
            return True
            
        except Exception as e:
            print(f"保存数据失败：{str(e)}")
            return False
    
    def update_user_input_data(self, user_input_data, project_data):
        """更新用户输入数据"""
        # 更新项目基本信息
        if "项目基本信息" in user_input_data:
            user_input_data["项目基本信息"]["项目名称"]["数值"] = project_data.get('project_name')
            user_input_data["项目基本信息"]["项目生命周期"]["数值"] = self.parse_number(project_data.get('project_life'))
            user_input_data["项目基本信息"]["项目人数"]["数值"] = self.parse_number(project_data.get('project_people'))
            user_input_data["项目基本信息"]["方案个数"]["数值"] = self.parse_number(project_data.get('scheme_count'))
        
        # 更新财税与融资参数
        if "财税与融资参数" in user_input_data:
            user_input_data["财税与融资参数"]["增值税率"]["数值"] = self.parse_number(project_data.get('vat_rate'))
            user_input_data["财税与融资参数"]["企业所得税率"]["数值"] = self.parse_number(project_data.get('income_tax_rate'))
            user_input_data["财税与融资参数"]["增值税附加税率"]["数值"] = self.parse_number(project_data.get('vat_additional_rate'))
            user_input_data["财税与融资参数"]["自有资金比例"]["数值"] = self.parse_number(project_data.get('equity_ratio'))
            user_input_data["财税与融资参数"]["贷款利率"]["数值"] = self.parse_number(project_data.get('loan_rate'))
        
        # 更新财务分析参数
        if "财务分析参数" in user_input_data:
            user_input_data["财务分析参数"]["名义贴现率"]["数值"] = self.parse_number(project_data.get('nominal_discount_rate'))
            user_input_data["财务分析参数"]["预期通货膨胀率"]["选择状态"] = project_data.get('inflation_rate_enabled', True)
            if project_data.get('inflation_rate_enabled'):
                user_input_data["财务分析参数"]["预期通货膨胀率"]["数值"] = self.parse_number(project_data.get('inflation_rate'))
        
        # 更新价格参数
        if "价格参数" in user_input_data:
            user_input_data["价格参数"]["氧气的销售价格"]["数值"] = self.parse_price_list(project_data.get('oxygen_price'))
            user_input_data["价格参数"]["电能销售价格"]["数值"] = self.parse_price_list(project_data.get('electricity_sell_price'))
            user_input_data["价格参数"]["电能的购买价格"]["数值"] = self.parse_price_list(project_data.get('electricity_buy_price'))
            user_input_data["价格参数"]["单位质量氢能的价格"]["数值"] = self.parse_price_list(project_data.get('hydrogen_price'))
        
        # 更新成本参数
        if "成本参数" in user_input_data:
            # 更新成本参数的选择状态
            if "场地购置费用" in user_input_data["成本参数"]:
                user_input_data["成本参数"]["场地购置费用"]["选择状态"] = project_data.get('site_cost_enabled', True)
            if "工程施工费用" in user_input_data["成本参数"]:
                user_input_data["成本参数"]["工程施工费用"]["选择状态"] = project_data.get('construction_cost_enabled', True)
            
            # 更新成本参数的数值
            user_input_data["成本参数"]["场地购置费用"]["数值"] = self.parse_number(project_data.get('site_cost'))
            user_input_data["成本参数"]["工程施工费用"]["数值"] = self.parse_number(project_data.get('construction_cost'))
            user_input_data["成本参数"]["年人员费用"]["数值"] = self.parse_number(project_data.get('personnel_cost'))
        
        # 更新设备参数
        self.update_equipment_data(user_input_data, project_data)
        
        # 更新设备选择状态
        self.update_equipment_selection(user_input_data, project_data)
    
    def update_equipment_data(self, user_input_data, project_data):
        """更新设备参数数据"""
        # WT参数
        if "WT" in user_input_data:
            user_input_data["WT"]["设备使用寿命"]["数值"] = self.parse_number(project_data.get('wt_lifetime'))
            user_input_data["WT"]["单位容量投资成本"]["数值"] = self.parse_number(project_data.get('wt_investment_cost'))
            user_input_data["WT"]["单位容量维护成本"]["数值"] = self.parse_number(project_data.get('wt_maintenance_cost'))
            user_input_data["WT"]["单位容量残值系数"]["数值"] = self.parse_number(project_data.get('wt_residual_value'))
            user_input_data["WT"]["风力发电总装机"]["数值"] = self.parse_capacity_list(project_data.get('wt_total_capacity'))
            # 更新电力电子接口装置的选择状态和数值
            if "电力电子接口装置成本设备成本的比例" in user_input_data["WT"]:
                user_input_data["WT"]["电力电子接口装置成本设备成本的比例"]["选择状态"] = project_data.get('wt_power_electronics_enabled', True)
                user_input_data["WT"]["电力电子接口装置成本设备成本的比例"]["数值"] = self.parse_number(project_data.get('wt_power_electronics_ratio'))
    
        # PV参数
        if "PV" in user_input_data:
            user_input_data["PV"]["设备使用寿命"]["数值"] = self.parse_number(project_data.get('pv_lifetime'))
            user_input_data["PV"]["单位容量投资成本"]["数值"] = self.parse_number(project_data.get('pv_investment_cost'))
            user_input_data["PV"]["单位容量维护成本"]["数值"] = self.parse_number(project_data.get('pv_maintenance_cost'))
            user_input_data["PV"]["单位容量残值系数"]["数值"] = self.parse_number(project_data.get('pv_residual_value'))
            user_input_data["PV"]["光伏机组总装机"]["数值"] = self.parse_capacity_list(project_data.get('pv_total_capacity'))
            # 更新电力电子接口装置的选择状态和数值
            if "电力电子接口装置成本设备成本的比例" in user_input_data["PV"]:
                user_input_data["PV"]["电力电子接口装置成本设备成本的比例"]["选择状态"] = project_data.get('pv_power_electronics_enabled', True)
                user_input_data["PV"]["电力电子接口装置成本设备成本的比例"]["数值"] = self.parse_number(project_data.get('pv_power_electronics_ratio'))
    
        # EL参数
        if "EL" in user_input_data:
            user_input_data["EL"]["设备使用寿命"]["数值"] = self.parse_number(project_data.get('el_lifetime'))
            user_input_data["EL"]["单位容量投资成本"]["数值"] = self.parse_number(project_data.get('el_investment_cost'))
            user_input_data["EL"]["单位容量维护成本"]["数值"] = self.parse_number(project_data.get('el_maintenance_cost'))
            user_input_data["EL"]["单位容量残值系数"]["数值"] = self.parse_number(project_data.get('el_residual_value'))
            user_input_data["EL"]["电解槽配置容量"]["数值"] = self.parse_capacity_list(project_data.get('el_capacity'))
            # 更新电力电子接口装置的选择状态和数值
            if "电力电子接口装置成本设备成本的比例" in user_input_data["EL"]:
                user_input_data["EL"]["电力电子接口装置成本设备成本的比例"]["选择状态"] = project_data.get('el_power_electronics_enabled', True)
                user_input_data["EL"]["电力电子接口装置成本设备成本的比例"]["数值"] = self.parse_number(project_data.get('el_power_electronics_ratio'))
    
        # HES参数
        if "HES" in user_input_data:
            user_input_data["HES"]["设备使用寿命"]["数值"] = self.parse_number(project_data.get('hes_lifetime'))
            user_input_data["HES"]["单位容量投资成本"]["数值"] = self.parse_number(project_data.get('hes_investment_cost'))
            user_input_data["HES"]["单位容量维护成本"]["数值"] = self.parse_number(project_data.get('hes_maintenance_cost'))
            user_input_data["HES"]["单位容量残值系数"]["数值"] = self.parse_number(project_data.get('hes_residual_value'))
            user_input_data["HES"]["氢储能装置配置容量"]["数值"] = self.parse_capacity_list(project_data.get('hes_capacity'))
    
        # HFC参数
        if "HFC" in user_input_data:
            user_input_data["HFC"]["设备使用寿命"]["数值"] = self.parse_number(project_data.get('hfc_lifetime'))
            user_input_data["HFC"]["单位容量投资成本"]["数值"] = self.parse_number(project_data.get('hfc_investment_cost'))
            user_input_data["HFC"]["单位容量维护成本"]["数值"] = self.parse_number(project_data.get('hfc_maintenance_cost'))
            user_input_data["HFC"]["单位容量残值系数"]["数值"] = self.parse_number(project_data.get('hfc_residual_value'))
            user_input_data["HFC"]["燃料电池配置容量"]["数值"] = self.parse_capacity_list(project_data.get('hfc_capacity'))
            # 更新电力电子接口装置的选择状态和数值
            if "电力电子接口装置成本设备成本的比例" in user_input_data["HFC"]:
                user_input_data["HFC"]["电力电子接口装置成本设备成本的比例"]["选择状态"] = project_data.get('hfc_power_electronics_enabled', True)
                user_input_data["HFC"]["电力电子接口装置成本设备成本的比例"]["数值"] = self.parse_number(project_data.get('hfc_power_electronics_ratio'))
    
        # ESS参数
        if "ESS" in user_input_data:
            user_input_data["ESS"]["蓄电池充放电效率"]["数值"] = self.parse_number(project_data.get('ess_efficiency'))
            user_input_data["ESS"]["设备使用寿命"]["数值"] = self.parse_number(project_data.get('ess_lifetime'))
            user_input_data["ESS"]["单位容量投资成本"]["数值"] = self.parse_number(project_data.get('ess_investment_cost'))
            user_input_data["ESS"]["蓄电池单位运行成本"]["数值"] = self.parse_number(project_data.get('ess_operation_cost'))
            user_input_data["ESS"]["单位容量残值系数"]["数值"] = self.parse_number(project_data.get('ess_residual_value'))
            user_input_data["ESS"]["蓄电池配置容量"]["数值"] = self.parse_capacity_list(project_data.get('ess_capacity'))
            # 更新电力电子接口装置的选择状态和数值
            if "电力电子接口装置成本设备成本的比例" in user_input_data["ESS"]:
                user_input_data["ESS"]["电力电子接口装置成本设备成本的比例"]["选择状态"] = project_data.get('ess_power_electronics_enabled', True)
                user_input_data["ESS"]["电力电子接口装置成本设备成本的比例"]["数值"] = self.parse_number(project_data.get('ess_power_electronics_ratio'))

    def update_equipment_selection(self, user_input_data, project_data):
        """更新设备选择状态"""
        # 更新设备选择状态
        if "WT" in user_input_data:
            user_input_data["WT"]["设备选择状态"] = project_data.get('wind_turbine', False)
        if "PV" in user_input_data:
            user_input_data["PV"]["设备选择状态"] = project_data.get('pv', False)
        if "EL" in user_input_data:
            user_input_data["EL"]["设备选择状态"] = project_data.get('electrolyzer', False)
        if "HES" in user_input_data:
            user_input_data["HES"]["设备选择状态"] = project_data.get('hydrogen_storage', False)
        if "HFC" in user_input_data:
            user_input_data["HFC"]["设备选择状态"] = project_data.get('fuel_cell', False)
        if "ESS" in user_input_data:
            user_input_data["ESS"]["设备选择状态"] = project_data.get('battery_storage', False)
        if "外部电网" in user_input_data:
            user_input_data["外部电网"]["设备选择状态"] = project_data.get('external_grid', True)
        if "外部氢源" in user_input_data:
            user_input_data["外部氢源"]["设备选择状态"] = project_data.get('external_hydrogen', True)
        
        # 更新负荷选择状态
        if "氧负荷" in user_input_data and "售氧" in user_input_data["氧负荷"]:
            user_input_data["氧负荷"]["售氧"]["设备选择状态"] = project_data.get('oxygen_load', False)
        
        if "氢负荷" in user_input_data:
            hydrogen_loads = user_input_data["氢负荷"]
            if "合成氨" in hydrogen_loads:
                hydrogen_loads["合成氨"]["设备选择状态"] = project_data.get('ammonia_load', False)
            if "合成甲醇" in hydrogen_loads:
                hydrogen_loads["合成甲醇"]["设备选择状态"] = project_data.get('methanol_load', False)
            if "成品油加工" in hydrogen_loads:
                hydrogen_loads["成品油加工"]["设备选择状态"] = project_data.get('oil_refining_load', False)
            if "燃料电池汽车加氢" in hydrogen_loads:
                hydrogen_loads["燃料电池汽车加氢"]["设备选择状态"] = project_data.get('vehicle_hydrogen_load', False)
            if "钢铁冶炼" in hydrogen_loads:
                hydrogen_loads["钢铁冶炼"]["设备选择状态"] = project_data.get('steel_load', False)
            if "其他用途售氢" in hydrogen_loads:
                hydrogen_loads["其他用途售氢"]["设备选择状态"] = project_data.get('other_hydrogen_load', False)
        
        if "电负荷" in user_input_data and "系统内用电单元" in user_input_data["电负荷"]:
            user_input_data["电负荷"]["系统内用电单元"]["设备选择状态"] = project_data.get('electrical_load', False)
    
    def update_indicator_data(self, indicator_system_data, indicator_data):
        """更新指标数据"""
        # 获取选中的指标列表
        selected_indicators = indicator_data.get('selected_indicators', [])
        
        # 指标ID与指标编码的映射关系
        indicator_mapping = {
            'initial_investment': 'A1',
            'annual_maintenance': 'A2', 
            'energy_purchase': 'A3',
            'npv': 'A4',
            'irr': 'A5',
            'dpp': 'A6',
            'energy_supply_ratio': 'B1',
            'battery_utilization': 'B2',
            'hydrogen_utilization': 'B3',
            'equivalent_hours': 'B4',
            'renewable_ratio': 'C1'
        }
        
        # 为所有指标设置选择状态
        for category, indicators in indicator_system_data.items():
            if isinstance(indicators, dict):
                for indicator_name, indicator_info in indicators.items():
                    if isinstance(indicator_info, dict) and "选择状态" in indicator_info:
                        indicator_code = indicator_info.get("指标编码", "")
                        
                        # 查找对应的指标ID
                        indicator_id = None
                        for id_key, code_value in indicator_mapping.items():
                            if code_value == indicator_code:
                                indicator_id = id_key
                                break
                        
                        # 设置选择状态
                        if indicator_id:
                            indicator_info["选择状态"] = indicator_id in selected_indicators
                        else:
                            # 如果没有找到对应的映射，默认为False
                            indicator_info["选择状态"] = False

    def parse_number(self, value):
        """解析数值，如果是None或空字符串则返回None"""
        if value is None or value == "":
            return None
        try:
            if isinstance(value, str):
                value = value.strip()
                if value == "":
                    return None
            return float(value)
        except (ValueError, TypeError):
            return None
    
    def parse_price_list(self, value):
        """解析价格列表，返回24小时的价格数组"""
        # 默认返回24个0.0
        default_list = [0.0] * 24
        
        if value is None or value == "":
            return default_list
        
        if isinstance(value, list):
            # 如果已经是列表，确保长度为24
            if len(value) == 24:
                return [float(v) if v is not None else 0.0 for v in value]
            else:
                # 调整列表长度为24
                result = [float(v) if v is not None else 0.0 for v in value]
                if len(result) < 24:
                    # 不足24个则用最后一个值填充
                    last_value = result[-1] if result else 0.0
                    result.extend([last_value] * (24 - len(result)))
                return result[:24]  # 截断为24个值
        
        try:
            if isinstance(value, str):
                value = value.strip()
                if value == "":
                    return default_list
            
                # 检查是否包含逗号分隔符
                if ',' in value:
                    # 尝试解析为逗号分隔的字符串
                    values = value.split(',')
                    result = []
                    
                    for v in values:
                        try:
                            result.append(float(v.strip()))
                        except (ValueError, TypeError):
                            result.append(0.0)
                    
                    # 调整长度为24
                    if len(result) < 24:
                        last_value = result[-1] if result else 0.0
                        result.extend([last_value] * (24 - len(result)))
                    return result[:24]  # 截断为24个值
                else:
                    # 如果是单个数值，复制24次
                    single_value = float(value)
                    return [single_value] * 24
            else:
                # 如果是单个数值，复制24次
                single_value = float(value)
                return [single_value] * 24
        except (ValueError, TypeError, IndexError):
            return default_list
    
    def parse_capacity_list(self, value):
        """解析容量列表，根据方案数量返回对应数组"""
        if value is None or value == "":
            return None
        
        if isinstance(value, list):
            return [float(v) if v is not None else 0.0 for v in value]
        
        try:
            if isinstance(value, str):
                value = value.strip()
                if value == "":
                    return None
                
                # 检查是否包含逗号分隔符
                if ',' in value:
                    # 解析逗号分隔的字符串
                    values = value.split(',')
                    result = []
                    for v in values:
                        try:
                            result.append(float(v.strip()))
                        except (ValueError, TypeError):
                            result.append(0.0)
                    return result
                else:
                    # 单个数值
                    return [float(value)]
            else:
                # 如果是单个数值，返回包含这个值的列表
                return [float(value)]
        except (ValueError, TypeError):
            return None
    
    def load_project(self, project_path):
        """加载项目"""
        try:
            self.current_project_path = project_path
            
            # 加载User_input.json
            user_input_path = os.path.join(project_path, "User_input.json")
            if os.path.exists(user_input_path):
                with open(user_input_path, 'r', encoding='utf-8') as f:
                    self.project_data = json.load(f)
            
            # 加载IndicatorSystem.json
            indicator_path = os.path.join(project_path, "IndicatorSystem.json")
            if os.path.exists(indicator_path):
                with open(indicator_path, 'r', encoding='utf-8') as f:
                    self.indicator_data = json.load(f)
            
            return True
            
        except Exception as e:
            print(f"加载项目失败：{str(e)}")
            return False
    
    def get_project_data(self):
        """获取项目数据"""
        return self.project_data
    
    def get_indicator_data(self):
        """获取指标数据"""
        return self.indicator_data
    
    def get_project_data_for_ui(self):
        """获取用于UI显示的项目数据"""
        if not self.project_data:
            return {}
        
        ui_data = {}
        
        # 项目基本信息
        if "项目基本信息" in self.project_data:
            basic_info = self.project_data["项目基本信息"]
            ui_data['project_name'] = basic_info.get("项目名称", {}).get("数值", "")
            ui_data['project_life'] = str(basic_info.get("项目生命周期", {}).get("数值", "")) if basic_info.get("项目生命周期", {}).get("数值") else ""
            ui_data['project_people'] = str(basic_info.get("项目人数", {}).get("数值", "")) if basic_info.get("项目人数", {}).get("数值") else ""
            ui_data['scheme_count'] = str(basic_info.get("方案个数", {}).get("数值", "")) if basic_info.get("方案个数", {}).get("数值") else ""  # 修正：使用正确的字段名
    
        # 财税与融资参数
        if "财税与融资参数" in self.project_data:
            tax_finance = self.project_data["财税与融资参数"]
            ui_data['vat_rate'] = str(tax_finance.get("增值税率", {}).get("数值", "")) if tax_finance.get("增值税率", {}).get("数值") else ""
            ui_data['income_tax_rate'] = str(tax_finance.get("企业所得税率", {}).get("数值", "")) if tax_finance.get("企业所得税率", {}).get("数值") else ""
            ui_data['vat_additional_rate'] = str(tax_finance.get("增值税附加税率", {}).get("数值", "")) if tax_finance.get("增值税附加税率", {}).get("数值") else ""
            ui_data['equity_ratio'] = str(tax_finance.get("自有资金比例", {}).get("数值", "")) if tax_finance.get("自有资金比例", {}).get("数值") else ""
            ui_data['loan_rate'] = str(tax_finance.get("贷款利率", {}).get("数值", "")) if tax_finance.get("贷款利率", {}).get("数值") else ""
        
        # 财务分析参数
        if "财务分析参数" in self.project_data:
            financial_analysis = self.project_data["财务分析参数"]
            ui_data['nominal_discount_rate'] = str(financial_analysis.get("名义贴现率", {}).get("数值", "")) if financial_analysis.get("名义贴现率", {}).get("数值") else ""
            inflation_rate_value = financial_analysis.get("预期通货膨胀率", {}).get("数值")
            ui_data['inflation_rate'] = str(inflation_rate_value) if inflation_rate_value is not None else ""
            ui_data['inflation_rate_enabled'] = financial_analysis.get("预期通货膨胀率", {}).get("选择状态", True)
        
        # 价格参数
        if "价格参数" in self.project_data:
            price_params = self.project_data["价格参数"]
            ui_data['oxygen_price'] = self.format_price_list(price_params.get("氧气的销售价格", {}).get("数值", []))
            ui_data['electricity_sell_price'] = self.format_price_list(price_params.get("电能销售价格", {}).get("数值", []))
            ui_data['electricity_buy_price'] = self.format_price_list(price_params.get("电能的购买价格", {}).get("数值", []))
            ui_data['hydrogen_price'] = self.format_price_list(price_params.get("单位质量氢能的价格", {}).get("数值", []))
        
        # 成本参数
        if "成本参数" in self.project_data:
            cost_params = self.project_data["成本参数"]
            ui_data['site_cost'] = str(cost_params.get("场地购置费用", {}).get("数值", "")) if cost_params.get("场地购置费用", {}).get("数值") else ""
            ui_data['construction_cost'] = str(cost_params.get("工程施工费用", {}).get("数值", "")) if cost_params.get("工程施工费用", {}).get("数值") else ""
            ui_data['personnel_cost'] = str(cost_params.get("年人员费用", {}).get("数值", "")) if cost_params.get("年人员费用", {}).get("数值") else ""
            # 成本参数选择状态
            ui_data['site_cost_enabled'] = cost_params.get("场地购置费用", {}).get("选择状态", True)
            ui_data['construction_cost_enabled'] = cost_params.get("工程施工费用", {}).get("选择状态", True)
        
        # 设备选择状态
        equipment_mapping = {
            'wind_turbine': 'WT',
            'pv': 'PV',
            'electrolyzer': 'EL',
            'hydrogen_storage': 'HES',
            'fuel_cell': 'HFC',
            'battery_storage': 'ESS',
            'external_grid': '外部电网',
            'external_hydrogen': '外部氢源'
        }
        
        for ui_key, data_key in equipment_mapping.items():
            if data_key in self.project_data:
                ui_data[ui_key] = self.project_data[data_key].get("设备选择状态", False)
        
        # 设备参数
        self.extract_equipment_params_for_ui(ui_data)
        
        # 负荷选择状态
        self.extract_load_params_for_ui(ui_data)
        
        return ui_data
    
    def extract_equipment_params_for_ui(self, ui_data):
        """提取设备参数用于UI显示"""
        # WT参数
        if "WT" in self.project_data:
            wt_data = self.project_data["WT"]
            ui_data['wt_lifetime'] = str(wt_data.get("设备使用寿命", {}).get("数值", "")) if wt_data.get("设备使用寿命", {}).get("数值") else ""
            ui_data['wt_investment_cost'] = str(wt_data.get("单位容量投资成本", {}).get("数值", "")) if wt_data.get("单位容量投资成本", {}).get("数值") else ""
            ui_data['wt_maintenance_cost'] = str(wt_data.get("单位容量维护成本", {}).get("数值", "")) if wt_data.get("单位容量维护成本", {}).get("数值") else ""
            ui_data['wt_residual_value'] = str(wt_data.get("单位容量残值系数", {}).get("数值", "")) if wt_data.get("单位容量残值系数", {}).get("数值") else ""
            ui_data['wt_total_capacity'] = self.format_capacity_list(wt_data.get("风力发电总装机", {}).get("数值"))
            # 添加电力电子接口装置选择状态和数值
            ui_data['wt_power_electronics_enabled'] = wt_data.get("电力电子接口装置成本设备成本的比例", {}).get("选择状态", False)
            ui_data['wt_power_electronics_ratio'] = str(wt_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值", "")) if wt_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值") else ""
        
        # PV参数
        if "PV" in self.project_data:
            pv_data = self.project_data["PV"]
            ui_data['pv_lifetime'] = str(pv_data.get("设备使用寿命", {}).get("数值", "")) if pv_data.get("设备使用寿命", {}).get("数值") else ""
            ui_data['pv_investment_cost'] = str(pv_data.get("单位容量投资成本", {}).get("数值", "")) if pv_data.get("单位容量投资成本", {}).get("数值") else ""
            ui_data['pv_maintenance_cost'] = str(pv_data.get("单位容量维护成本", {}).get("数值", "")) if pv_data.get("单位容量维护成本", {}).get("数值") else ""
            ui_data['pv_residual_value'] = str(pv_data.get("单位容量残值系数", {}).get("数值", "")) if pv_data.get("单位容量残值系数", {}).get("数值") else ""
            ui_data['pv_total_capacity'] = self.format_capacity_list(pv_data.get("光伏机组总装机", {}).get("数值"))
            # 添加电力电子接口装置选择状态和数值
            ui_data['pv_power_electronics_enabled'] = pv_data.get("电力电子接口装置成本设备成本的比例", {}).get("选择状态", False)
            ui_data['pv_power_electronics_ratio'] = str(pv_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值", "")) if pv_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值") else ""
        
        # EL参数
        if "EL" in self.project_data:
            el_data = self.project_data["EL"]
            ui_data['el_lifetime'] = str(el_data.get("设备使用寿命", {}).get("数值", "")) if el_data.get("设备使用寿命", {}).get("数值") else ""
            ui_data['el_efficiency'] = str(el_data.get("能量转化系数", {}).get("数值", "")) if el_data.get("能量转化系数", {}).get("数值") else ""
            ui_data['el_investment_cost'] = str(el_data.get("单位容量投资成本", {}).get("数值", "")) if el_data.get("单位容量投资成本", {}).get("数值") else ""
            ui_data['el_maintenance_cost'] = str(el_data.get("单位容量维护成本", {}).get("数值", "")) if el_data.get("单位容量维护成本", {}).get("数值") else ""
            ui_data['el_residual_value'] = str(el_data.get("单位容量残值系数", {}).get("数值", "")) if el_data.get("单位容量残值系数", {}).get("数值") else ""
            ui_data['el_capacity'] = self.format_capacity_list(el_data.get("电解槽配置容量", {}).get("数值"))  # 修正：使用正确的字段名
            # 添加电力电子接口装置选择状态和数值
            ui_data['el_power_electronics_enabled'] = el_data.get("电力电子接口装置成本设备成本的比例", {}).get("选择状态", False)
            ui_data['el_power_electronics_ratio'] = str(el_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值", "")) if el_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值") else ""
        
        # HES参数
        if "HES" in self.project_data:
            hes_data = self.project_data["HES"]
            ui_data['hes_lifetime'] = str(hes_data.get("设备使用寿命", {}).get("数值", "")) if hes_data.get("设备使用寿命", {}).get("数值") else ""
            ui_data['hes_investment_cost'] = str(hes_data.get("单位容量投资成本", {}).get("数值", "")) if hes_data.get("单位容量投资成本", {}).get("数值") else ""
            ui_data['hes_maintenance_cost'] = str(hes_data.get("单位容量维护成本", {}).get("数值", "")) if hes_data.get("单位容量维护成本", {}).get("数值") else ""
            ui_data['hes_residual_value'] = str(hes_data.get("单位容量残值系数", {}).get("数值", "")) if hes_data.get("单位容量残值系数", {}).get("数值") else ""
            ui_data['hes_capacity'] = self.format_capacity_list(hes_data.get("氢储能装置配置容量", {}).get("数值"))  # 修正：使用正确的字段名
    
        # HFC参数
        if "HFC" in self.project_data:
            hfc_data = self.project_data["HFC"]
            ui_data['hfc_lifetime'] = str(hfc_data.get("设备使用寿命", {}).get("数值", "")) if hfc_data.get("设备使用寿命", {}).get("数值") else ""
            ui_data['hfc_investment_cost'] = str(hfc_data.get("单位容量投资成本", {}).get("数值", "")) if hfc_data.get("单位容量投资成本", {}).get("数值") else ""
            ui_data['hfc_maintenance_cost'] = str(hfc_data.get("单位容量维护成本", {}).get("数值", "")) if hfc_data.get("单位容量维护成本", {}).get("数值") else ""
            ui_data['hfc_residual_value'] = str(hfc_data.get("单位容量残值系数", {}).get("数值", "")) if hfc_data.get("单位容量残值系数", {}).get("数值") else ""
            ui_data['hfc_capacity'] = self.format_capacity_list(hfc_data.get("燃料电池配置容量", {}).get("数值"))  # 修正：使用正确的字段名
            # 添加电力电子接口装置选择状态和数值
            ui_data['hfc_power_electronics_enabled'] = hfc_data.get("电力电子接口装置成本设备成本的比例", {}).get("选择状态", False)
            ui_data['hfc_power_electronics_ratio'] = str(hfc_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值", "")) if hfc_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值") else ""
        
        # ESS参数
        if "ESS" in self.project_data:
            ess_data = self.project_data["ESS"]
            ui_data['ess_efficiency'] = str(ess_data.get("蓄电池充放电效率", {}).get("数值", "")) if ess_data.get("蓄电池充放电效率", {}).get("数值") else ""
            ui_data['ess_operation_cost'] = str(ess_data.get("蓄电池单位运行成本", {}).get("数值", "")) if ess_data.get("蓄电池单位运行成本", {}).get("数值") else ""
            ui_data['ess_lifetime'] = str(ess_data.get("设备使用寿命", {}).get("数值", "")) if ess_data.get("设备使用寿命", {}).get("数值") else ""
            ui_data['ess_investment_cost'] = str(ess_data.get("单位容量投资成本", {}).get("数值", "")) if ess_data.get("单位容量投资成本", {}).get("数值") else ""
            ui_data['ess_residual_value'] = str(ess_data.get("单位容量残值系数", {}).get("数值", "")) if ess_data.get("单位容量残值系数", {}).get("数值") else ""
            ui_data['ess_capacity'] = self.format_capacity_list(ess_data.get("蓄电池配置容量", {}).get("数值"))
            # 添加电力电子接口装置选择状态和数值
            ui_data['ess_power_electronics_enabled'] = ess_data.get("电力电子接口装置成本设备成本的比例", {}).get("选择状态", False)
            ui_data['ess_power_electronics_ratio'] = str(ess_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值", "")) if ess_data.get("电力电子接口装置成本设备成本的比例", {}).get("数值") else ""

    def extract_load_params_for_ui(self, ui_data):
        """提取负荷参数用于UI显示"""
        # 氧负荷
        if "氧负荷" in self.project_data and "售氧" in self.project_data["氧负荷"]:
            ui_data['oxygen_load'] = self.project_data["氧负荷"]["售氧"].get("设备选择状态", False)
        else:
            ui_data['oxygen_load'] = False  # 默认为False，除非JSON中明确指定为True
    
        # 氢负荷
        if "氢负荷" in self.project_data:
            hydrogen_loads = self.project_data["氢负荷"]
            ui_data['ammonia_load'] = hydrogen_loads.get("合成氨", {}).get("设备选择状态", False)
            ui_data['methanol_load'] = hydrogen_loads.get("合成甲醇", {}).get("设备选择状态", False)
            ui_data['oil_refining_load'] = hydrogen_loads.get("成品油加工", {}).get("设备选择状态", False)
            ui_data['vehicle_hydrogen_load'] = hydrogen_loads.get("燃料电池汽车加氢", {}).get("设备选择状态", False)
            ui_data['steel_load'] = hydrogen_loads.get("钢铁冶炼", {}).get("设备选择状态", False)
            ui_data['other_hydrogen_load'] = hydrogen_loads.get("其他用途售氢", {}).get("设备选择状态", False)
        else:
            # 如果JSON中没有氢负荷数据，则所有选项默认为False
            ui_data['ammonia_load'] = False
            ui_data['methanol_load'] = False
            ui_data['oil_refining_load'] = False
            ui_data['vehicle_hydrogen_load'] = False
            ui_data['steel_load'] = False
            ui_data['other_hydrogen_load'] = False
    
        # 电负荷
        if "电负荷" in self.project_data and "系统内用电单元" in self.project_data["电负荷"]:
            ui_data['electrical_load'] = self.project_data["电负荷"]["系统内用电单元"].get("设备选择状态", False)
        else:
            ui_data['electrical_load'] = False  # 默认为False，除非JSON中明确指定为True
    
    def get_indicator_data_for_ui(self):
        """获取用于UI显示的指标数据"""
        if not self.indicator_data:
            return {'selected_indicators': []}
        
        selected_indicators = []
        indicator_mapping = {
            'A1': 'initial_investment',
            'A2': 'annual_maintenance', 
            'A3': 'energy_purchase',
            'A4': 'npv',
            'A5': 'irr',
            'A6': 'dpp',
            'B1': 'energy_supply_ratio',
            'B2': 'battery_utilization',
            'B3': 'hydrogen_utilization',
            'B4': 'equivalent_hours',
            'C1': 'renewable_ratio'
        }
        
        for category, indicators in self.indicator_data.items():
            if isinstance(indicators, dict):
                for indicator_name, indicator_info in indicators.items():
                    if isinstance(indicator_info, dict) and indicator_info.get("选择状态", False):
                        indicator_code = indicator_info.get("指标编码", "")
                        if indicator_code in indicator_mapping:
                            selected_indicators.append(indicator_mapping[indicator_code])
        
        return {'selected_indicators': selected_indicators}
    
    def format_price_list(self, price_list):
        """格式化价格列表为字符串"""
        if not price_list or not isinstance(price_list, list):
            return ""
        
        # 确保总是返回24个值的逗号分隔字符串
        if isinstance(price_list, list):
            # 补全或截断为24个值
            if len(price_list) < 24:
                # 如果不足24个值，用最后一个值填充
                last_value = price_list[-1] if price_list else 0.0
                price_list = price_list + [last_value] * (24 - len(price_list))
            elif len(price_list) > 24:
                # 如果超过24个值，截断
                price_list = price_list[:24]
            
            # 将所有值格式化为字符串并用逗号连接
            return ",".join(str(float(x)) for x in price_list)
        
        return ""
    
    def format_capacity_list(self, capacity_list):
        """格式化容量列表为字符串"""
        if not capacity_list:
            return ""
        
        if isinstance(capacity_list, list):
            return ",".join(str(x) for x in capacity_list)
        else:
            return str(capacity_list)