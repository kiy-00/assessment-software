import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QLabel, QLineEdit, QGroupBox, QCheckBox, QPushButton,
                             QScrollArea, QFrame, QComboBox, QSpinBox, QDoubleSpinBox,
                             QTextEdit, QSplitter)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont

class ProjectDesignPage(QWidget):
    """项目参数设计页面"""
    
    data_updated = pyqtSignal()  # 数据更新信号
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_connections()
    
    def init_ui(self):
        """初始化用户界面"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # 创建顶部项目名称输入区域
        self.create_project_header(main_layout)
        
        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 创建内容区域
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(15)
        
        # 创建各个参数组
        self.create_basic_info_group(content_layout)
        self.create_tax_finance_group(content_layout)
        self.create_financial_analysis_group(content_layout)
        self.create_price_parameters_group(content_layout)
        self.create_cost_parameters_group(content_layout)
        self.create_system_topology_group(content_layout)
        self.create_equipment_parameters_group(content_layout)
        self.create_external_energy_group(content_layout)
        self.create_energy_consumption_group(content_layout)
        
        # 创建底部按钮
        self.create_bottom_buttons(content_layout)
        
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
    
    def create_project_header(self, parent_layout):
        """创建项目头部信息"""
        header_frame = QFrame()
        header_frame.setFrameStyle(QFrame.Box)
        header_frame.setStyleSheet("QFrame { border: 1px solid #ddd; background-color: #f9f9f9; }")
        
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(15, 10, 15, 10)
        
        # 项目名称标签和输入框
        project_label = QLabel("项目名称：")
        project_label.setFont(QFont("微软雅黑", 10, QFont.Bold))
        
        self.project_name_edit = QLineEdit()
        self.project_name_edit.setText("新项目_f8ba97")
        self.project_name_edit.setFixedWidth(200)
        
        header_layout.addWidget(project_label)
        header_layout.addWidget(self.project_name_edit)
        header_layout.addStretch()
        
        parent_layout.addWidget(header_frame)
    
    def create_basic_info_group(self, parent_layout):
        """创建项目基本信息组"""
        group = QGroupBox("项目基本信息")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        layout.setSpacing(10)
        
        # 项目生命周期
        layout.addWidget(QLabel("项目生命周期（年）"), 0, 0)
        self.project_life_edit = QLineEdit()
        layout.addWidget(self.project_life_edit, 0, 1)
        
        # 项目人数
        layout.addWidget(QLabel("项目人数（人）"), 1, 0)
        self.project_people_edit = QLineEdit()
        layout.addWidget(self.project_people_edit, 1, 1)
        
        parent_layout.addWidget(group)
    
    def create_tax_finance_group(self, parent_layout):
        """创建财税与融资参数组"""
        group = QGroupBox("财税与融资参数")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        layout.setSpacing(10)
        
        # 增值税率
        layout.addWidget(QLabel("增值税率（%）"), 0, 0)
        self.vat_rate_edit = QLineEdit()
        layout.addWidget(self.vat_rate_edit, 0, 1)
        
        # 企业所得税率
        layout.addWidget(QLabel("企业所得税率（%）"), 1, 0)
        self.income_tax_rate_edit = QLineEdit()
        layout.addWidget(self.income_tax_rate_edit, 1, 1)
        
        # 增值税附加税率
        layout.addWidget(QLabel("增值税附加税率（%）"), 2, 0)
        self.vat_additional_rate_edit = QLineEdit()
        layout.addWidget(self.vat_additional_rate_edit, 2, 1)
        
        # 自有资金比例
        layout.addWidget(QLabel("自有资金比例（%）"), 3, 0)
        self.equity_ratio_edit = QLineEdit()
        layout.addWidget(self.equity_ratio_edit, 3, 1)
        
        # 贷款利率
        layout.addWidget(QLabel("贷款利率（%）"), 4, 0)
        self.loan_rate_edit = QLineEdit()
        layout.addWidget(self.loan_rate_edit, 4, 1)
        
        parent_layout.addWidget(group)
    
    def create_financial_analysis_group(self, parent_layout):
        """创建财务分析参数组"""
        group = QGroupBox("财务分析参数")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        layout.setSpacing(10)
        
        # 名义贴现率
        layout.addWidget(QLabel("名义贴现率（%）"), 0, 0)
        self.nominal_discount_rate_edit = QLineEdit()
        layout.addWidget(self.nominal_discount_rate_edit, 0, 1)
        
        # 预期通货膨胀率
        layout.addWidget(QLabel("预期通货膨胀率（%）"), 1, 0)
        self.inflation_rate_edit = QLineEdit()
        layout.addWidget(self.inflation_rate_edit, 1, 1)
        
        parent_layout.addWidget(group)
    
    def create_price_parameters_group(self, parent_layout):
        """创建价格参数组"""
        group = QGroupBox("价格参数")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QVBoxLayout(group)
        
        # 添加说明文字
        note_label = QLabel("※在输入框中输入价格的24h分时数据，使用半角逗号\",\"隔开")
        note_label.setStyleSheet("QLabel { color: #666; font-size: 9px; }")
        layout.addWidget(note_label)
        
        grid_layout = QGridLayout()
        
        # 氧气的销售价格
        grid_layout.addWidget(QLabel("氧气的销售价格（元/kg）"), 0, 0)
        self.oxygen_price_edit = QLineEdit()
        grid_layout.addWidget(self.oxygen_price_edit, 0, 1)
        
        # 电能销售价格
        grid_layout.addWidget(QLabel("电能销售价格（元/kW·h）"), 1, 0)
        self.electricity_sell_price_edit = QLineEdit()
        grid_layout.addWidget(self.electricity_sell_price_edit, 1, 1)
        
        # 电能的购买价格
        grid_layout.addWidget(QLabel("电能的购买价格（元/kW·h）"), 2, 0)
        self.electricity_buy_price_edit = QLineEdit()
        grid_layout.addWidget(self.electricity_buy_price_edit, 2, 1)
        
        # 单位质量氢能的价格
        grid_layout.addWidget(QLabel("单位质量氢能的价格（元/kg）"), 3, 0)
        self.hydrogen_price_edit = QLineEdit()
        grid_layout.addWidget(self.hydrogen_price_edit, 3, 1)
        
        layout.addLayout(grid_layout)
        parent_layout.addWidget(group)
    
    def create_cost_parameters_group(self, parent_layout):
        """创建成本参数组"""
        group = QGroupBox("成本参数")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        layout.setSpacing(10)
        
        # 场地购置费用
        self.site_cost_checkbox = QCheckBox("场地购置费用（万元）")
        layout.addWidget(self.site_cost_checkbox, 0, 0)
        self.site_cost_edit = QLineEdit()
        layout.addWidget(self.site_cost_edit, 0, 1)
        
        # 工程施工费用
        self.construction_cost_checkbox = QCheckBox("工程施工费用（万元）")
        layout.addWidget(self.construction_cost_checkbox, 1, 0)
        self.construction_cost_edit = QLineEdit()
        layout.addWidget(self.construction_cost_edit, 1, 1)
        
        # 年人员费用
        layout.addWidget(QLabel("年人员费用（万元/年·人）"), 2, 0)
        self.personnel_cost_edit = QLineEdit()
        layout.addWidget(self.personnel_cost_edit, 2, 1)
        
        parent_layout.addWidget(group)
    
    def create_system_topology_group(self, parent_layout):
        """创建系统拓扑设计组"""
        group = QGroupBox("系统拓扑设计")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        main_layout = QHBoxLayout(group)
        
        # 系统结构单元选择
        left_frame = QFrame()
        left_layout = QVBoxLayout(left_frame)
        left_layout.addWidget(QLabel("系统结构单元选择："))
        
        self.wind_turbine_checkbox = QCheckBox("风力发电单元(WT)")
        self.wind_turbine_checkbox.setChecked(True)
        left_layout.addWidget(self.wind_turbine_checkbox)
        
        self.pv_checkbox = QCheckBox("光伏机组(PV)")
        left_layout.addWidget(self.pv_checkbox)
        
        self.electrolyzer_checkbox = QCheckBox("电解槽(EL)")
        left_layout.addWidget(self.electrolyzer_checkbox)
        
        self.hydrogen_storage_checkbox = QCheckBox("氢储能系统(HES)")
        left_layout.addWidget(self.hydrogen_storage_checkbox)
        
        self.fuel_cell_checkbox = QCheckBox("氢燃料电池(HFC)")
        self.fuel_cell_checkbox.setChecked(True)
        left_layout.addWidget(self.fuel_cell_checkbox)
        
        self.battery_storage_checkbox = QCheckBox("电储能系统(ESS)")
        self.battery_storage_checkbox.setChecked(True)
        left_layout.addWidget(self.battery_storage_checkbox)
        
        self.external_grid_checkbox = QCheckBox("外部电网")
        self.external_grid_checkbox.setChecked(True)
        left_layout.addWidget(self.external_grid_checkbox)
        
        self.external_hydrogen_checkbox = QCheckBox("外部氢网")
        self.external_hydrogen_checkbox.setChecked(True)
        left_layout.addWidget(self.external_hydrogen_checkbox)
        
        # 消费侧设计
        right_frame = QFrame()
        right_layout = QVBoxLayout(right_frame)
        right_layout.addWidget(QLabel("消费侧设计："))
        
        # 氧负荷组
        oxygen_group = QGroupBox("氧负荷")
        oxygen_layout = QVBoxLayout(oxygen_group)
        self.oxygen_sell_checkbox = QCheckBox("售氧")
        oxygen_layout.addWidget(self.oxygen_sell_checkbox)
        right_layout.addWidget(oxygen_group)
        
        # 氢负荷组
        hydrogen_group = QGroupBox("氢负荷")
        hydrogen_layout = QGridLayout(hydrogen_group)
        self.ammonia_checkbox = QCheckBox("合成氨")
        self.ammonia_checkbox.setChecked(True)
        hydrogen_layout.addWidget(self.ammonia_checkbox, 0, 0)
        
        self.fuel_cell_vehicle_checkbox = QCheckBox("燃料电池汽车加氢")
        hydrogen_layout.addWidget(self.fuel_cell_vehicle_checkbox, 0, 1)
        
        self.methanol_checkbox = QCheckBox("合成甲醇")
        hydrogen_layout.addWidget(self.methanol_checkbox, 1, 0)
        
        self.steel_making_checkbox = QCheckBox("钢铁冶炼")
        hydrogen_layout.addWidget(self.steel_making_checkbox, 1, 1)
        
        self.oil_processing_checkbox = QCheckBox("成品油加工")
        hydrogen_layout.addWidget(self.oil_processing_checkbox, 2, 0)
        
        self.other_hydrogen_checkbox = QCheckBox("其他用途售氢")
        hydrogen_layout.addWidget(self.other_hydrogen_checkbox, 2, 1)
        
        right_layout.addWidget(hydrogen_group)
        
        # 电负荷组
        power_group = QGroupBox("电负荷")
        power_layout = QVBoxLayout(power_group)
        self.internal_power_checkbox = QCheckBox("系统内用电单元")
        self.internal_power_checkbox.setChecked(True)
        power_layout.addWidget(self.internal_power_checkbox)
        right_layout.addWidget(power_group)
        
        main_layout.addWidget(left_frame)
        main_layout.addWidget(right_frame)
        parent_layout.addWidget(group)
    
    def create_equipment_parameters_group(self, parent_layout):
        """创建设备参数组"""
        # WT参数
        self.create_wt_parameters(parent_layout)
        
        # PV参数
        self.create_pv_parameters(parent_layout)
        
        # ESS参数
        self.create_ess_parameters(parent_layout)
        
        # HES参数
        self.create_hes_parameters(parent_layout)
        
        # EL参数
        self.create_el_parameters(parent_layout)
        
        # HFC参数
        self.create_hfc_parameters(parent_layout)
    
    def create_wt_parameters(self, parent_layout):
        """创建风电参数组"""
        group = QGroupBox("WT")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        
        # 风力发电单元出力
        layout.addWidget(QLabel("风力发电单元出力（kW）"), 0, 0)
        list_input_btn = QPushButton("在列表中输入各方案数据")
        list_input_btn.setMaximumWidth(150)
        layout.addWidget(list_input_btn, 0, 1)
        
        # 设备使用寿命
        layout.addWidget(QLabel("设备使用寿命（年）"), 1, 0)
        self.wt_lifetime_edit = QLineEdit()
        layout.addWidget(self.wt_lifetime_edit, 1, 1)
        
        # 电力电子接口装置成本
        self.wt_power_electronics_checkbox = QCheckBox("电力电子接口装置成本设备成本的比例（%）")
        layout.addWidget(self.wt_power_electronics_checkbox, 2, 0)
        self.wt_power_electronics_edit = QLineEdit()
        layout.addWidget(self.wt_power_electronics_edit, 2, 1)
        
        # 单位容量投资成本
        layout.addWidget(QLabel("单位容量投资成本（万元）"), 3, 0)
        self.wt_investment_cost_edit = QLineEdit()
        layout.addWidget(self.wt_investment_cost_edit, 3, 1)
        
        # 单位容量维护成本
        layout.addWidget(QLabel("单位容量维护成本（万元）"), 4, 0)
        self.wt_maintenance_cost_edit = QLineEdit()
        layout.addWidget(self.wt_maintenance_cost_edit, 4, 1)
        
        # 单位容量残值系数
        layout.addWidget(QLabel("单位容量残值系数（%）"), 5, 0)
        self.wt_residual_value_edit = QLineEdit()
        layout.addWidget(self.wt_residual_value_edit, 5, 1)
        
        # 说明文字和总装机
        note_label = QLabel("※在输入框中输入各方案WT容量，使用半角逗号\",\"隔开")
        note_label.setStyleSheet("QLabel { color: #666; font-size: 9px; }")
        layout.addWidget(note_label, 6, 0, 1, 2)
        
        layout.addWidget(QLabel("风力发电总装机（kW）"), 7, 0)
        self.wt_total_capacity_edit = QLineEdit()
        self.wt_total_capacity_edit.setText("123，342，456")
        layout.addWidget(self.wt_total_capacity_edit, 7, 1)
        
        parent_layout.addWidget(group)
    
    def create_pv_parameters(self, parent_layout):
        """创建光伏参数组"""
        group = QGroupBox("PV")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        
        # 光伏机组出力
        layout.addWidget(QLabel("光伏机组出力（kW）"), 0, 0)
        list_input_btn = QPushButton("在列表中输入各方案数据")
        list_input_btn.setMaximumWidth(150)
        layout.addWidget(list_input_btn, 0, 1)
        
        # 设备使用寿命
        layout.addWidget(QLabel("设备使用寿命（年）"), 1, 0)
        self.pv_lifetime_edit = QLineEdit()
        layout.addWidget(self.pv_lifetime_edit, 1, 1)
        
        # 电力电子接口装置成本
        self.pv_power_electronics_checkbox = QCheckBox("电力电子接口装置成本设备成本的比例（%）")
        layout.addWidget(self.pv_power_electronics_checkbox, 2, 0)
        self.pv_power_electronics_edit = QLineEdit()
        layout.addWidget(self.pv_power_electronics_edit, 2, 1)
        
        # 单位容量投资成本
        layout.addWidget(QLabel("单位容量投资成本（元/kW）"), 3, 0)
        self.pv_investment_cost_edit = QLineEdit()
        layout.addWidget(self.pv_investment_cost_edit, 3, 1)
        
        # 单位容量维护成本
        layout.addWidget(QLabel("单位容量维护成本（元/kW）"), 4, 0)
        self.pv_maintenance_cost_edit = QLineEdit()
        layout.addWidget(self.pv_maintenance_cost_edit, 4, 1)
        
        # 单位容量残值系数
        layout.addWidget(QLabel("单位容量残值系数（%）"), 5, 0)
        self.pv_residual_value_edit = QLineEdit()
        layout.addWidget(self.pv_residual_value_edit, 5, 1)
        
        # 说明文字和总装机
        note_label = QLabel("※在输入框中输入各方案PV容量，使用半角逗号\",\"隔开")
        note_label.setStyleSheet("QLabel { color: #666; font-size: 9px; }")
        layout.addWidget(note_label, 6, 0, 1, 2)
        
        layout.addWidget(QLabel("光伏机组总装机（kW）"), 7, 0)
        self.pv_total_capacity_edit = QLineEdit()
        layout.addWidget(self.pv_total_capacity_edit, 7, 1)
        
        parent_layout.addWidget(group)
    
    def create_ess_parameters(self, parent_layout):
        """创建电储能参数组"""
        group = QGroupBox("ESS")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        
        # ESS的充放功率
        layout.addWidget(QLabel("ESS的充放功率（kW）"), 0, 0)
        list_input_btn = QPushButton("在列表中输入各方案数据")
        list_input_btn.setMaximumWidth(150)
        layout.addWidget(list_input_btn, 0, 1)
        
        # 蓄电池充放电效率
        layout.addWidget(QLabel("蓄电池充放电效率（%）"), 1, 0)
        self.ess_efficiency_edit = QLineEdit()
        layout.addWidget(self.ess_efficiency_edit, 1, 1)
        
        # 蓄电池单位运行成本
        layout.addWidget(QLabel("蓄电池单位运行成本（元/kW）"), 2, 0)
        self.ess_operation_cost_edit = QLineEdit()
        layout.addWidget(self.ess_operation_cost_edit, 2, 1)
        
        # 设备使用寿命
        layout.addWidget(QLabel("设备使用寿命（年）"), 3, 0)
        self.ess_lifetime_edit = QLineEdit()
        layout.addWidget(self.ess_lifetime_edit, 3, 1)
        
        # 电力电子接口装置成本
        self.ess_power_electronics_checkbox = QCheckBox("电力电子接口装置成本设备成本的比例（%）")
        layout.addWidget(self.ess_power_electronics_checkbox, 4, 0)
        self.ess_power_electronics_edit = QLineEdit()
        layout.addWidget(self.ess_power_electronics_edit, 4, 1)
        
        # 设备单位容量投资成本
        layout.addWidget(QLabel("设备单位容量投资成本（万元）"), 5, 0)
        self.ess_investment_cost_edit = QLineEdit()
        layout.addWidget(self.ess_investment_cost_edit, 5, 1)
        
        # 说明文字和总容量
        note_label = QLabel("※在输入框中输入各方案ESS容量，使用半角逗号\",\"隔开")
        note_label.setStyleSheet("QLabel { color: #666; font-size: 9px; }")
        layout.addWidget(note_label, 6, 0, 1, 2)
        
        layout.addWidget(QLabel("电储能装置总容量（kW）"), 7, 0)
        self.ess_total_capacity_edit = QLineEdit()
        layout.addWidget(self.ess_total_capacity_edit, 7, 1)
        
        parent_layout.addWidget(group)
    
    def create_hes_parameters(self, parent_layout):
        """创建氢储能参数组"""
        group = QGroupBox("HES")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        
        # 氢储能装置加氢放氢
        layout.addWidget(QLabel("氢储能装置加氢放氢（kg）"), 0, 0)
        list_input_btn = QPushButton("在列表中输入各方案数据")
        list_input_btn.setMaximumWidth(150)
        layout.addWidget(list_input_btn, 0, 1)
        
        # 设备使用寿命
        layout.addWidget(QLabel("设备使用寿命（年）"), 1, 0)
        self.hes_lifetime_edit = QLineEdit()
        layout.addWidget(self.hes_lifetime_edit, 1, 1)
        
        # 单位容量投资成本
        layout.addWidget(QLabel("单位容量投资成本（万元）"), 2, 0)
        self.hes_investment_cost_edit = QLineEdit()
        layout.addWidget(self.hes_investment_cost_edit, 2, 1)
        
        # 单位容量维护成本
        layout.addWidget(QLabel("单位容量维护成本（万元）"), 3, 0)
        self.hes_maintenance_cost_edit = QLineEdit()
        layout.addWidget(self.hes_maintenance_cost_edit, 3, 1)
        
        # 单位容量残值系数
        layout.addWidget(QLabel("单位容量残值系数（%）"), 4, 0)
        self.hes_residual_value_edit = QLineEdit()
        layout.addWidget(self.hes_residual_value_edit, 4, 1)
        
        # 说明文字和配置容量
        note_label = QLabel("※在输入框中输入各方案EL容量，使用半角逗号\",\"隔开")
        note_label.setStyleSheet("QLabel { color: #666; font-size: 9px; }")
        layout.addWidget(note_label, 6, 0, 1, 2)
        
        layout.addWidget(QLabel("电解槽配置容量（kW）"), 7, 0)
        self.el_total_capacity_edit = QLineEdit()
        layout.addWidget(self.el_total_capacity_edit, 7, 1)
        
        parent_layout.addWidget(group)
    
    def create_hfc_parameters(self, parent_layout):
        """创建燃料电池参数组"""
        group = QGroupBox("HFC")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        
        # 设备使用寿命
        layout.addWidget(QLabel("设备使用寿命（年）"), 0, 0)
        self.hfc_lifetime_edit = QLineEdit()
        layout.addWidget(self.hfc_lifetime_edit, 0, 1)
        
        # 电力电子接口装置成本
        self.hfc_power_electronics_checkbox = QCheckBox("电力电子接口装置成本设备成本的比例（%）")
        layout.addWidget(self.hfc_power_electronics_checkbox, 1, 0)
        self.hfc_power_electronics_edit = QLineEdit()
        layout.addWidget(self.hfc_power_electronics_edit, 1, 1)
        
        # 单位容量投资成本
        layout.addWidget(QLabel("单位容量投资成本（万元）"), 2, 0)
        self.hfc_investment_cost_edit = QLineEdit()
        layout.addWidget(self.hfc_investment_cost_edit, 2, 1)
        
        # 单位容量维护成本
        layout.addWidget(QLabel("单位容量维护成本（万元）"), 3, 0)
        self.hfc_maintenance_cost_edit = QLineEdit()
        layout.addWidget(self.hfc_maintenance_cost_edit, 3, 1)
        
        # 单位容量残值系数
        layout.addWidget(QLabel("单位容量残值系数（%）"), 4, 0)
        self.hfc_residual_value_edit = QLineEdit()
        layout.addWidget(self.hfc_residual_value_edit, 4, 1)
        
        # 说明文字和配置容量
        note_label = QLabel("※在输入框中输入各方案HFC容量，使用半角逗号\",\"隔开")
        note_label.setStyleSheet("QLabel { color: #666; font-size: 9px; }")
        layout.addWidget(note_label, 5, 0, 1, 2)
        
        layout.addWidget(QLabel("燃料电池配置容量（kW）"), 6, 0)
        self.hfc_total_capacity_edit = QLineEdit()
        layout.addWidget(self.hfc_total_capacity_edit, 6, 1)
        
        parent_layout.addWidget(group)
    
    def create_external_energy_group(self, parent_layout):
        """创建外部能源网组"""
        group = QGroupBox("外部能源网")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        
        # 系统与外部氢源的交互质量
        layout.addWidget(QLabel("系统与外部氢源的交互质量（kg）"), 0, 0)
        hydrogen_input_btn = QPushButton("在列表中输入各方案数据")
        hydrogen_input_btn.setMaximumWidth(150)
        layout.addWidget(hydrogen_input_btn, 0, 1)
        
        # 系统与外部电网的交互功率
        layout.addWidget(QLabel("系统与外部电网的交互功率（kW）"), 1, 0)
        power_input_btn = QPushButton("在列表中输入各方案数据")
        power_input_btn.setMaximumWidth(150)
        layout.addWidget(power_input_btn, 1, 1)
        
        parent_layout.addWidget(group)
    
    def create_energy_consumption_group(self, parent_layout):
        """创建能源消费侧组"""
        group = QGroupBox("能源消费侧")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QVBoxLayout(group)
        
        # 氧负荷
        oxygen_frame = QFrame()
        oxygen_frame.setFrameStyle(QFrame.Box)
        oxygen_layout = QGridLayout(oxygen_frame)
        oxygen_layout.addWidget(QLabel("氧负荷"), 0, 0, 1, 2)
        
        oxygen_layout.addWidget(QLabel("销售氧气的质量（kg）"), 1, 0)
        oxygen_sell_btn = QPushButton("在列表中输入各方案数据")
        oxygen_sell_btn.setMaximumWidth(150)
        oxygen_layout.addWidget(oxygen_sell_btn, 1, 1)
        
        layout.addWidget(oxygen_frame)
        
        # 氢负荷
        hydrogen_frame = QFrame()
        hydrogen_frame.setFrameStyle(QFrame.Box)
        hydrogen_layout = QGridLayout(hydrogen_frame)
        hydrogen_layout.addWidget(QLabel("氢负荷"), 0, 0, 1, 2)
        
        # 添加各种氢负荷项目
        hydrogen_items = [
            "合成氨", "合成甲醇", "成品油加工", 
            "燃料电池汽车加氢", "钢铁冶炼", "其他用途售氢"
        ]
        
        for i, item in enumerate(hydrogen_items):
            row = i + 1
            hydrogen_layout.addWidget(QLabel(item), row, 0)
            btn = QPushButton("在列表中输入各方案数据")
            btn.setMaximumWidth(150)
            hydrogen_layout.addWidget(btn, row, 1)
        
        layout.addWidget(hydrogen_frame)
        
        # 电负荷
        power_frame = QFrame()
        power_frame.setFrameStyle(QFrame.Box)
        power_layout = QGridLayout(power_frame)
        power_layout.addWidget(QLabel("电负荷"), 0, 0, 1, 2)
        
        power_layout.addWidget(QLabel("电负荷所消耗的功率（kW）"), 1, 0)
        power_consumption_btn = QPushButton("在列表中输入各方案数据")
        power_consumption_btn.setMaximumWidth(150)
        power_layout.addWidget(power_consumption_btn, 1, 1)
        
        layout.addWidget(power_frame)
        parent_layout.addWidget(group)
    
    def create_bottom_buttons(self, parent_layout):
        """创建底部按钮"""
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        # 更新数据按钮
        self.update_data_btn = QPushButton("更新数据")
        self.update_data_btn.setMinimumSize(100, 35)
        self.update_data_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        self.update_data_btn.clicked.connect(self.update_data)
        
        button_layout.addWidget(self.update_data_btn)
        parent_layout.addLayout(button_layout)
    
    def setup_connections(self):
        """设置信号连接"""
        # 项目名称变化时发出信号
        self.project_name_edit.textChanged.connect(self.data_updated.emit)
        
        # 其他重要参数变化时发出信号
        self.project_life_edit.textChanged.connect(self.data_updated.emit)
        self.project_people_edit.textChanged.connect(self.data_updated.emit)
        
        # 系统拓扑选择变化时发出信号
        self.wind_turbine_checkbox.toggled.connect(self.on_system_topology_changed)
        self.pv_checkbox.toggled.connect(self.on_system_topology_changed)
        self.fuel_cell_checkbox.toggled.connect(self.on_system_topology_changed)
        self.battery_storage_checkbox.toggled.connect(self.on_system_topology_changed)
        
    def on_system_topology_changed(self):
        """系统拓扑发生变化时的处理"""
        self.data_updated.emit()
        # 这里可以添加根据选择的组件动态显示/隐藏相关参数组的逻辑
    
    def update_data(self):
        """更新数据"""
        print("更新项目参数数据...")
        # 这里可以添加数据验证和保存逻辑
        self.validate_and_save_data()
        self.data_updated.emit()
    
    def validate_and_save_data(self):
        """验证和保存数据"""
        # 获取所有输入数据
        project_data = self.get_project_data()
        
        # 验证数据
        if self.validate_data(project_data):
            print("数据验证通过")
            # 这里可以调用数据管理器保存数据
            return True
        else:
            print("数据验证失败")
            return False
    
    def get_project_data(self):
        """获取项目数据"""
        return {
            'project_name': self.project_name_edit.text(),
            'project_life': self.project_life_edit.text(),
            'project_people': self.project_people_edit.text(),
            'vat_rate': self.vat_rate_edit.text(),
            'income_tax_rate': self.income_tax_rate_edit.text(),
            'vat_additional_rate': self.vat_additional_rate_edit.text(),
            'equity_ratio': self.equity_ratio_edit.text(),
            'loan_rate': self.loan_rate_edit.text(),
            'nominal_discount_rate': self.nominal_discount_rate_edit.text(),
            'inflation_rate': self.inflation_rate_edit.text(),
            'oxygen_price': self.oxygen_price_edit.text(),
            'electricity_sell_price': self.electricity_sell_price_edit.text(),
            'electricity_buy_price': self.electricity_buy_price_edit.text(),
            'hydrogen_price': self.hydrogen_price_edit.text(),
            'site_cost': self.site_cost_edit.text(),
            'construction_cost': self.construction_cost_edit.text(),
            'personnel_cost': self.personnel_cost_edit.text(),
            # 系统拓扑选择
            'wind_turbine': self.wind_turbine_checkbox.isChecked(),
            'pv': self.pv_checkbox.isChecked(),
            'electrolyzer': self.electrolyzer_checkbox.isChecked(),
            'hydrogen_storage': self.hydrogen_storage_checkbox.isChecked(),
            'fuel_cell': self.fuel_cell_checkbox.isChecked(),
            'battery_storage': self.battery_storage_checkbox.isChecked(),
            'external_grid': self.external_grid_checkbox.isChecked(),
            'external_hydrogen': self.external_hydrogen_checkbox.isChecked(),
            # 消费侧选择
            'oxygen_sell': self.oxygen_sell_checkbox.isChecked(),
            'ammonia': self.ammonia_checkbox.isChecked(),
            'methanol': self.methanol_checkbox.isChecked(),
            'oil_processing': self.oil_processing_checkbox.isChecked(),
            'fuel_cell_vehicle': self.fuel_cell_vehicle_checkbox.isChecked(),
            'steel_making': self.steel_making_checkbox.isChecked(),
            'other_hydrogen': self.other_hydrogen_checkbox.isChecked(),
            'internal_power': self.internal_power_checkbox.isChecked(),
            # 设备参数
            'wt_lifetime': self.wt_lifetime_edit.text(),
            'wt_investment_cost': self.wt_investment_cost_edit.text(),
            'wt_maintenance_cost': self.wt_maintenance_cost_edit.text(),
            'wt_residual_value': self.wt_residual_value_edit.text(),
            'wt_total_capacity': self.wt_total_capacity_edit.text(),
            'pv_lifetime': self.pv_lifetime_edit.text(),
            'pv_investment_cost': self.pv_investment_cost_edit.text(),
            'pv_maintenance_cost': self.pv_maintenance_cost_edit.text(),
            'pv_residual_value': self.pv_residual_value_edit.text(),
            'pv_total_capacity': self.pv_total_capacity_edit.text(),
            'ess_efficiency': self.ess_efficiency_edit.text(),
            'ess_operation_cost': self.ess_operation_cost_edit.text(),
            'ess_lifetime': self.ess_lifetime_edit.text(),
            'ess_investment_cost': self.ess_investment_cost_edit.text(),
            'ess_total_capacity': self.ess_total_capacity_edit.text(),
            'hes_lifetime': self.hes_lifetime_edit.text(),
            'hes_investment_cost': self.hes_investment_cost_edit.text(),
            'hes_maintenance_cost': self.hes_maintenance_cost_edit.text(),
            'hes_residual_value': self.hes_residual_value_edit.text(),
            'hes_total_capacity': self.hes_total_capacity_edit.text(),
            'el_lifetime': self.el_lifetime_edit.text(),
            'el_efficiency': self.el_efficiency_edit.text(),
            'el_investment_cost': self.el_investment_cost_edit.text(),
            'el_maintenance_cost': self.el_maintenance_cost_edit.text(),
            'el_residual_value': self.el_residual_value_edit.text(),
            'el_total_capacity': self.el_total_capacity_edit.text(),
            'hfc_lifetime': self.hfc_lifetime_edit.text(),
            'hfc_investment_cost': self.hfc_investment_cost_edit.text(),
            'hfc_maintenance_cost': self.hfc_maintenance_cost_edit.text(),
            'hfc_residual_value': self.hfc_residual_value_edit.text(),
            'hfc_total_capacity': self.hfc_total_capacity_edit.text(),
        }
    
    def validate_data(self, data):
        """验证数据有效性"""
        # 检查必填项
        required_fields = ['project_name', 'project_life', 'project_people']
        for field in required_fields:
            if not data.get(field):
                print(f"缺少必填项: {field}")
                return False
        
        # 检查数值型字段
        numeric_fields = [
            'project_life', 'project_people', 'vat_rate', 'income_tax_rate',
            'vat_additional_rate', 'equity_ratio', 'loan_rate',
            'nominal_discount_rate', 'inflation_rate'
        ]
        for field in numeric_fields:
            value = data.get(field)
            if value:
                try:
                    float(value)
                except ValueError:
                    print(f"数值格式错误: {field}")
                    return False
        
        # 检查百分比字段范围
        percentage_fields = [
            'vat_rate', 'income_tax_rate', 'vat_additional_rate', 
            'equity_ratio', 'loan_rate', 'nominal_discount_rate', 'inflation_rate'
        ]
        for field in percentage_fields:
            value = data.get(field)
            if value:
                try:
                    val = float(value)
                    if val < 0 or val > 100:
                        print(f"百分比字段超出范围 (0-100): {field}")
                        return False
                except ValueError:
                    pass  # 已在上面检查过
        
        return True
    
    def load_project_data(self, data):
        """加载项目数据到界面"""
        if not data:
            return
        
        # 基本信息
        self.project_name_edit.setText(data.get('project_name', ''))
        self.project_life_edit.setText(data.get('project_life', ''))
        self.project_people_edit.setText(data.get('project_people', ''))
        
        # 财税参数
        self.vat_rate_edit.setText(data.get('vat_rate', ''))
        self.income_tax_rate_edit.setText(data.get('income_tax_rate', ''))
        self.vat_additional_rate_edit.setText(data.get('vat_additional_rate', ''))
        self.equity_ratio_edit.setText(data.get('equity_ratio', ''))
        self.loan_rate_edit.setText(data.get('loan_rate', ''))
        
        # 财务分析参数
        self.nominal_discount_rate_edit.setText(data.get('nominal_discount_rate', ''))
        self.inflation_rate_edit.setText(data.get('inflation_rate', ''))
        
        # 价格参数
        self.oxygen_price_edit.setText(data.get('oxygen_price', ''))
        self.electricity_sell_price_edit.setText(data.get('electricity_sell_price', ''))
        self.electricity_buy_price_edit.setText(data.get('electricity_buy_price', ''))
        self.hydrogen_price_edit.setText(data.get('hydrogen_price', ''))
        
        # 成本参数
        self.site_cost_edit.setText(data.get('site_cost', ''))
        self.construction_cost_edit.setText(data.get('construction_cost', ''))
        self.personnel_cost_edit.setText(data.get('personnel_cost', ''))
        
        # 系统拓扑
        self.wind_turbine_checkbox.setChecked(data.get('wind_turbine', False))
        self.pv_checkbox.setChecked(data.get('pv', False))
        self.electrolyzer_checkbox.setChecked(data.get('electrolyzer', False))
        self.hydrogen_storage_checkbox.setChecked(data.get('hydrogen_storage', False))
        self.fuel_cell_checkbox.setChecked(data.get('fuel_cell', False))
        self.battery_storage_checkbox.setChecked(data.get('battery_storage', False))
        self.external_grid_checkbox.setChecked(data.get('external_grid', False))
        self.external_hydrogen_checkbox.setChecked(data.get('external_hydrogen', False))
        
        # 消费侧
        self.oxygen_sell_checkbox.setChecked(data.get('oxygen_sell', False))
        self.ammonia_checkbox.setChecked(data.get('ammonia', False))
        self.methanol_checkbox.setChecked(data.get('methanol', False))
        self.oil_processing_checkbox.setChecked(data.get('oil_processing', False))
        self.fuel_cell_vehicle_checkbox.setChecked(data.get('fuel_cell_vehicle', False))
        self.steel_making_checkbox.setChecked(data.get('steel_making', False))
        self.other_hydrogen_checkbox.setChecked(data.get('other_hydrogen', False))
        self.internal_power_checkbox.setChecked(data.get('internal_power', False))
        
        # 设备参数
        self.wt_lifetime_edit.setText(data.get('wt_lifetime', ''))
        self.wt_investment_cost_edit.setText(data.get('wt_investment_cost', ''))
        self.wt_maintenance_cost_edit.setText(data.get('wt_maintenance_cost', ''))
        self.wt_residual_value_edit.setText(data.get('wt_residual_value', ''))
        self.wt_total_capacity_edit.setText(data.get('wt_total_capacity', ''))
        
        self.pv_lifetime_edit.setText(data.get('pv_lifetime', ''))
        self.pv_investment_cost_edit.setText(data.get('pv_investment_cost', ''))
        self.pv_maintenance_cost_edit.setText(data.get('pv_maintenance_cost', ''))
        self.pv_residual_value_edit.setText(data.get('pv_residual_value', ''))
        self.pv_total_capacity_edit.setText(data.get('pv_total_capacity', ''))
        
        self.ess_efficiency_edit.setText(data.get('ess_efficiency', ''))
        self.ess_operation_cost_edit.setText(data.get('ess_operation_cost', ''))
        self.ess_lifetime_edit.setText(data.get('ess_lifetime', ''))
        self.ess_investment_cost_edit.setText(data.get('ess_investment_cost', ''))
        self.ess_total_capacity_edit.setText(data.get('ess_total_capacity', ''))
        
        self.hes_lifetime_edit.setText(data.get('hes_lifetime', ''))
        self.hes_investment_cost_edit.setText(data.get('hes_investment_cost', ''))
        self.hes_maintenance_cost_edit.setText(data.get('hes_maintenance_cost', ''))
        self.hes_residual_value_edit.setText(data.get('hes_residual_value', ''))
        self.hes_total_capacity_edit.setText(data.get('hes_total_capacity', ''))
        
        self.el_lifetime_edit.setText(data.get('el_lifetime', ''))
        self.el_efficiency_edit.setText(data.get('el_efficiency', ''))
        self.el_investment_cost_edit.setText(data.get('el_investment_cost', ''))
        self.el_maintenance_cost_edit.setText(data.get('el_maintenance_cost', ''))
        self.el_residual_value_edit.setText(data.get('el_residual_value', ''))
        self.el_total_capacity_edit.setText(data.get('el_total_capacity', ''))
        
        self.hfc_lifetime_edit.setText(data.get('hfc_lifetime', ''))
        self.hfc_investment_cost_edit.setText(data.get('hfc_investment_cost', ''))
        self.hfc_maintenance_cost_edit.setText(data.get('hfc_maintenance_cost', ''))
        self.hfc_residual_value_edit.setText(data.get('hfc_residual_value', ''))
        self.hfc_total_capacity_edit.setText(data.get('hfc_total_capacity', ''))
    
    def reset_form(self):
        """重置表单"""
        # 清空所有输入框
        for widget in self.findChildren(QLineEdit):
            widget.clear()
        
        # 重置所有复选框
        for widget in self.findChildren(QCheckBox):
            widget.setChecked(False)
        
        # 设置默认项目名称
        self.project_name_edit.setText("新项目_" + str(hash(self))[-6:])
        
        # 设置默认选中项
        self.wind_turbine_checkbox.setChecked(True)
        self.fuel_cell_checkbox.setChecked(True)
        self.battery_storage_checkbox.setChecked(True)
        self.external_grid_checkbox.setChecked(True)
        self.external_hydrogen_checkbox.setChecked(True)
        self.ammonia_checkbox.setChecked(True)
        self.internal_power_checkbox.setChecked(True)

    def create_el_parameters(self, parent_layout):
        """创建电解槽参数组"""
        group = QGroupBox("EL")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        layout = QGridLayout(group)
        
        # 设备使用寿命
        layout.addWidget(QLabel("设备使用寿命（年）"), 0, 0)
        self.el_lifetime_edit = QLineEdit()
        layout.addWidget(self.el_lifetime_edit, 0, 1)
        
        # 能量转化系数
        layout.addWidget(QLabel("能量转化系数（%）"), 1, 0)
        self.el_efficiency_edit = QLineEdit()
        layout.addWidget(self.el_efficiency_edit, 1, 1)
        
        # 电力电子接口装置成本
        self.el_power_electronics_checkbox = QCheckBox("电力电子接口装置成本设备成本的比例（%）")
        layout.addWidget(self.el_power_electronics_checkbox, 2, 0)
        self.el_power_electronics_edit = QLineEdit()
        layout.addWidget(self.el_power_electronics_edit, 2, 1)
        
        # 单位容量投资成本
        layout.addWidget(QLabel("单位容量投资成本（万元）"), 3, 0)
        self.el_investment_cost_edit = QLineEdit()
        layout.addWidget(self.el_investment_cost_edit, 3, 1)
        
        # 单位容量维护成本
        layout.addWidget(QLabel("单位容量维护成本（万元）"), 4, 0)
        self.el_maintenance_cost_edit = QLineEdit()
        layout.addWidget(self.el_maintenance_cost_edit, 4, 1)
        
        # 单位容量残值系数
        layout.addWidget(QLabel("单位容量残值系数（%）"), 5, 0)
        self.el_residual_value_edit = QLineEdit()
        layout.addWidget(self.el_residual_value_edit, 5, 1)
        
        # 说明文字和配置容量
        note_label = QLabel("※在输入框中输入各方案HES容量，使用半角逗号\",\"隔开")


# 测试代码
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    # 创建测试窗口
    window = ProjectDesignPage()
    window.setWindowTitle("项目参数设计页面测试")
    window.resize(1000, 800)
    window.show()
    
    sys.exit(app.exec_())  # 运行应用程序
       
    
    
