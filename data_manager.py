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
            "ESS-电储能装置充放功率(kW).xlsx",
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
            
            # 添加表头
            ws['A1'] = "时间"
            ws['B1'] = "方案1"
            ws['C1'] = "方案2"
            ws['D1'] = "方案3"
            
            # 添加24小时时间
            for i in range(24):
                ws[f'A{i+2}'] = f"{i:02d}:00"
            
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
                "方案人数": {"单位": "个", "类型": "General", "选择状态": True, "数值": None, "备注": ""}
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
                "能量转化系数": {"单位": "1", "类型": "General", "选择状态": True, "数值": 39.4, "备注": ""},
                "电力电子接口装置成本设备成本的比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量维护成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "设备配置容量": {"单位": "kW", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "HES": {
                "设备选择状态": True,
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量维护成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "设备配置容量": {"单位": "kW", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "HFC": {
                "设备选择状态": True,
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "电力电子接口装置成本设备成本的比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量维护成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "单位容量残值系数": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "设备配置容量": {"单位": "kW", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "ESS": {
                "设备选择状态": True,
                "蓄电池充放电效率": {"单位": "kW", "类型": "General", "选择状态": True, "数值": 90, "备注": ""},
                "蓄电池单位运行成本": {"单位": "元", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "设备使用寿命": {"单位": "年", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "电力电子接口装置成本设备成本的比例": {"单位": "%", "类型": "General", "选择状态": True, "数值": 5, "备注": ""},
                "单位容量投资成本": {"单位": "元/kW", "类型": "General", "选择状态": True, "数值": None, "备注": ""},
                "设备配置容量": {"单位": "kW", "类型": "Particular", "选择状态": True, "数值": None, "备注": ""}
            },
            "外部电网": {"设备选择状态": True},
            "外部氢网": {"设备选择状态": True},
            "氧负荷": {"设备选择状态": True},
            "氢负荷": {
                "合成氨": {"设备选择状态": True},
                "合成甲醇": {"设备选择状态": True},
                "成品油加工": {"设备选择状态": True},
                "燃料电池汽车加氢": {"设备选择状态": True},
                "钢铁冶炼": {"设备选择状态": True},
                "其他用途售氢": {"设备选择状态": True}
            },
            "电负荷": {"设备选择状态": True}
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
        if "WT" in user_input_data and project_data.get('wind_turbine'):
            user_input_data["WT"]["设备使用寿命"]["数值"] = self.parse_number(project_data.get('wt_lifetime'))
            user_input_data["WT"]["单位容量投资成本"]["数值"] = self.parse_number(project_data.get('wt_investment_cost'))
            user_input_data["WT"]["单位容量维护成本"]["数值"] = self.parse_number(project_data.get('wt_maintenance_cost'))
            user_input_data["WT"]["单位容量残值系数"]["数值"] = self.parse_number(project_data.get('wt_residual_value'))
            user_input_data["WT"]["风力发电总装机"]["数值"] = self.parse_capacity_list(project_data.get('wt_total_capacity'))
        
        # 类似地更新其他设备参数...
    
    def update_equipment_selection(self, user_input_data, project_data):
        """更新设备选择状态"""
        if "WT" in user_input_data:
            user_input_data["WT"]["设备选择状态"] = project_data.get('wind_turbine', False)
        if "PV" in user_input_data:
            user_input_data["PV"]["设备选择状态"] = project_data.get('pv', False)
        if "HFC" in user_input_data:
            user_input_data["HFC"]["设备选择状态"] = project_data.get('fuel_cell', False)
        if "ESS" in user_input_data:
            user_input_data["ESS"]["设备选择状态"] = project_data.get('battery_storage', False)
        if "外部电网" in user_input_data:
            user_input_data["外部电网"]["设备选择状态"] = project_data.get('external_grid', False)
        if "外部氢网" in user_input_data:
            user_input_data["外部氢网"]["设备选择状态"] = project_data.get('external_hydrogen', False)
    
    def update_indicator_data(self, indicator_system_data, indicator_data):
        """更新指标系统数据"""
        selected_indicators = indicator_data.get('selected_indicators', [])
        
        # 更新财务效益指标
        if "财务效益指标" in indicator_system_data:
            for indicator_name, indicator_info in indicator_system_data["财务效益指标"].items():
                indicator_id = self.get_indicator_id_by_name(indicator_name)
                indicator_info["选择状态"] = indicator_id in selected_indicators
        
        # 更新技术效益指标
        if "技术效益指标" in indicator_system_data:
            for indicator_name, indicator_info in indicator_system_data["技术效益指标"].items():
                indicator_id = self.get_indicator_id_by_name(indicator_name)
                indicator_info["选择状态"] = indicator_id in selected_indicators
        
        # 更新环境效益指标
        if "环境效益指标" in indicator_system_data:
            for indicator_name, indicator_info in indicator_system_data["环境效益指标"].items():
                indicator_id = self.get_indicator_id_by_name(indicator_name)
                indicator_info["选择状态"] = indicator_id in selected_indicators
    
    def get_indicator_id_by_name(self, indicator_name):
        """根据指标名称获取指标ID"""
        indicator_mapping = {
            "初始投资成本": "initial_investment",
            "内部收益率": "irr",
            "投资回收期": "dpp",
            "净现值": "npv",
            "年运维成本": "annual_maintenance",
            "能源外购成本": "energy_purchase",
            "能源网供应占比": "energy_supply_ratio",
            "电储能利用水平": "battery_utilization",
            "氢储能利用水平": "hydrogen_utilization",
            "等效可利用小时数": "equivalent_hours",
            "可再生能源供应占比": "renewable_ratio"
        }
        return indicator_mapping.get(indicator_name, "")
    
    def parse_number(self, value):
        """解析数字"""
        if value is None or value == '':
            return None
        try:
            return float(value)
        except:
            return None
    
    def parse_price_list(self, value):
        """解析价格列表（24小时分时数据）"""
        if value is None or value == '':
            return None
        try:
            # 如果是字符串，尝试按逗号分割
            if isinstance(value, str):
                prices = [float(x.strip()) for x in value.split(',') if x.strip()]
                # 如果不足24个值，用最后一个值填充
                if len(prices) < 24:
                    last_value = prices[-1] if prices else 0
                    prices.extend([last_value] * (24 - len(prices)))
                return prices[:24]  # 只取前24个值
            else:
                return None
        except:
            return None
    
    def parse_capacity_list(self, value):
        """解析容量列表（多方案数据）"""
        if value is None or value == '':
            return None
        try:
            # 如果是字符串，尝试按逗号分割
            if isinstance(value, str):
                # 替换中文逗号为英文逗号
                value = value.replace('，', ',')
                capacities = [float(x.strip()) for x in value.split(',') if x.strip()]
                return capacities
            else:
                return None
        except:
            return None
    
    def load_project(self, project_path):
        """加载项目数据"""
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
    
    def get_project_data_for_ui(self):
        """获取用于UI显示的项目数据"""
        if not self.project_data:
            return {}
        
        ui_data = {}
        
        # 项目基本信息
        if "项目基本信息" in self.project_data:
            ui_data['project_name'] = self.project_data["项目基本信息"]["项目名称"]["数值"] or ""
            ui_data['project_life'] = str(self.project_data["项目基本信息"]["项目生命周期"]["数值"] or "")
            ui_data['project_people'] = str(self.project_data["项目基本信息"]["项目人数"]["数值"] or "")
        
        # 财税与融资参数
        if "财税与融资参数" in self.project_data:
            ui_data['vat_rate'] = str(self.project_data["财税与融资参数"]["增值税率"]["数值"] or "")
            ui_data['income_tax_rate'] = str(self.project_data["财税与融资参数"]["企业所得税率"]["数值"] or "")
            ui_data['vat_additional_rate'] = str(self.project_data["财税与融资参数"]["增值税附加税率"]["数值"] or "")
            ui_data['equity_ratio'] = str(self.project_data["财税与融资参数"]["自有资金比例"]["数值"] or "")
            ui_data['loan_rate'] = str(self.project_data["财税与融资参数"]["贷款利率"]["数值"] or "")
        
        # 添加更多数据转换...
        
        return ui_data
    
    def get_indicator_data_for_ui(self):
        """获取用于UI显示的指标数据"""
        if not self.indicator_data:
            return {'selected_indicators': []}
        
        selected_indicators = []
        
        # 遍历所有指标类别
        for category in self.indicator_data.values():
            for indicator_name, indicator_info in category.items():
                if indicator_info.get("选择状态", False):
                    indicator_id = self.get_indicator_id_by_name(indicator_name)
                    if indicator_id:
                        selected_indicators.append(indicator_id)
        
        return {'selected_indicators': selected_indicators}