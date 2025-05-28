import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QLabel, QLineEdit, QGroupBox, QCheckBox, QPushButton,
                             QScrollArea, QFrame, QListWidget, QListWidgetItem,
                             QStackedWidget, QButtonGroup)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

class IndicatorManagementPage(QWidget):
    """指标管理页面"""
    
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
        
        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")
        
        # 创建内容部件
        content_widget = QWidget()
        content_widget_layout = QVBoxLayout(content_widget)
        content_widget_layout.setSpacing(20)
        
        # 创建各个指标组
        self.create_financial_indicators(content_widget_layout)
        self.create_technical_indicators(content_widget_layout)
        self.create_environmental_indicators(content_widget_layout)
        
        # 创建更新数据按钮
        self.create_update_button(content_widget_layout)
        
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
    
    def create_financial_indicators(self, parent_layout):
        """创建财务效益指标组"""
        group = QGroupBox("财务效益指标")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #cccccc;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 20px;
                padding: 0 10px 0 10px;
            }
        """)
        
        layout = QGridLayout(group)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 创建指标项
        indicators = [
            ("初始投资成本", "initial_investment"),
            ("内部收益率IRR", "irr"),
            ("投资回收期DPP", "dpp"),
            ("净现值NPV", "npv"),
            ("年运维成本", "annual_maintenance"),
            ("能源外购成本", "energy_purchase")
        ]
        
        row = 0
        for indicator_name, indicator_id in indicators:
            # 复选框
            checkbox = QCheckBox()
            checkbox.setChecked(True)
            checkbox.setObjectName(f"checkbox_{indicator_id}")
            layout.addWidget(checkbox, row, 0)
            
            # 指标名称
            label = QLabel(indicator_name)
            label.setFont(QFont("微软雅黑", 9))
            layout.addWidget(label, row, 1)
            
            # 指标详情按钮
            detail_btn = QPushButton("指标详情")
            detail_btn.setObjectName(f"detail_{indicator_id}")
            detail_btn.setFixedWidth(120)
            detail_btn.setStyleSheet(self.get_detail_button_style())
            detail_btn.clicked.connect(lambda checked, ind=indicator_name: self.show_indicator_detail(ind))
            layout.addWidget(detail_btn, row, 2)
            
            row += 1
        
        # 设置列宽比例
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 2)
        
        parent_layout.addWidget(group)
    
    def create_technical_indicators(self, parent_layout):
        """创建技术效益指标组"""
        group = QGroupBox("技术效益指标")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #cccccc;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 20px;
                padding: 0 10px 0 10px;
            }
        """)
        
        layout = QGridLayout(group)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 创建指标项
        indicators = [
            ("能源网供应占比", "energy_supply_ratio"),
            ("电储能利用水平", "battery_utilization"),
            ("氢储能利用水平", "hydrogen_utilization"),
            ("等效可利用小时数", "equivalent_hours")
        ]
        
        row = 0
        for indicator_name, indicator_id in indicators:
            # 复选框
            checkbox = QCheckBox()
            checkbox.setChecked(True)
            checkbox.setObjectName(f"checkbox_{indicator_id}")
            layout.addWidget(checkbox, row, 0)
            
            # 指标名称
            label = QLabel(indicator_name)
            label.setFont(QFont("微软雅黑", 9))
            layout.addWidget(label, row, 1)
            
            # 指标详情按钮
            detail_btn = QPushButton("指标详情")
            detail_btn.setObjectName(f"detail_{indicator_id}")
            detail_btn.setFixedWidth(120)
            detail_btn.setStyleSheet(self.get_detail_button_style())
            detail_btn.clicked.connect(lambda checked, ind=indicator_name: self.show_indicator_detail(ind))
            layout.addWidget(detail_btn, row, 2)
            
            row += 1
        
        # 设置列宽比例
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 2)
        
        parent_layout.addWidget(group)
    
    def create_environmental_indicators(self, parent_layout):
        """创建环境效益指标组"""
        group = QGroupBox("环境效益指标")
        group.setFont(QFont("微软雅黑", 10, QFont.Bold))
        group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #cccccc;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 20px;
                padding: 0 10px 0 10px;
            }
        """)
        
        layout = QGridLayout(group)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 创建指标项
        indicators = [
            ("可再生能源供应占比", "renewable_ratio")
        ]
        
        row = 0
        for indicator_name, indicator_id in indicators:
            # 复选框
            checkbox = QCheckBox()
            checkbox.setChecked(True)
            checkbox.setObjectName(f"checkbox_{indicator_id}")
            layout.addWidget(checkbox, row, 0)
            
            # 指标名称
            label = QLabel(indicator_name)
            label.setFont(QFont("微软雅黑", 9))
            layout.addWidget(label, row, 1)
            
            # 指标详情按钮
            detail_btn = QPushButton("指标详情")
            detail_btn.setObjectName(f"detail_{indicator_id}")
            detail_btn.setFixedWidth(120)
            detail_btn.setStyleSheet(self.get_detail_button_style())
            detail_btn.clicked.connect(lambda checked, ind=indicator_name: self.show_indicator_detail(ind))
            layout.addWidget(detail_btn, row, 2)
            
            row += 1
        
        # 设置列宽比例
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 2)
        
        parent_layout.addWidget(group)
    
    def create_update_button(self, parent_layout):
        """创建更新数据按钮"""
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        self.update_btn = QPushButton("更新数据")
        self.update_btn.setMinimumSize(120, 35)
        self.update_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        self.update_btn.clicked.connect(self.update_data)
        
        button_layout.addWidget(self.update_btn)
        parent_layout.addLayout(button_layout)
    
    def get_detail_button_style(self):
        """获取详情按钮样式"""
        return """
            QPushButton {
                background-color: #ecf0f1;
                color: #2c3e50;
                border: 1px solid #bdc3c7;
                border-radius: 3px;
                padding: 5px 15px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #d5dbdb;
            }
            QPushButton:pressed {
                background-color: #aeb6bf;
            }
        """
    
    def setup_connections(self):
        """设置信号连接"""
        # 这里可以添加各个复选框状态变化的连接
        for checkbox in self.findChildren(QCheckBox):
            if checkbox.objectName().startswith("checkbox_"):
                checkbox.toggled.connect(self.on_indicator_selection_changed)
    
    def on_indicator_selection_changed(self):
        """指标选择变化时的处理"""
        self.data_updated.emit()
    
    def show_indicator_detail(self, indicator_name):
        """显示指标详情"""
        print(f"显示 {indicator_name} 的详情")
        # 这里可以打开一个对话框显示指标的详细信息
    
    def update_data(self):
        """更新数据"""
        print("更新指标数据...")
        # 收集所有选中的指标
        selected_indicators = self.get_selected_indicators()
        print(f"已选中的指标: {selected_indicators}")
        self.data_updated.emit()
    
    def get_selected_indicators(self):
        """获取所有选中的指标"""
        selected = []
        
        # 遍历所有复选框
        for checkbox in self.findChildren(QCheckBox):
            if checkbox.isChecked() and checkbox.objectName().startswith("checkbox_"):
                indicator_id = checkbox.objectName().replace("checkbox_", "")
                selected.append(indicator_id)
        
        return selected
    
    def set_selected_indicators(self, indicators):
        """设置选中的指标"""
        # 先取消所有选中
        for checkbox in self.findChildren(QCheckBox):
            if checkbox.objectName().startswith("checkbox_"):
                checkbox.setChecked(False)
        
        # 设置指定的指标为选中
        for indicator_id in indicators:
            checkbox = self.findChild(QCheckBox, f"checkbox_{indicator_id}")
            if checkbox:
                checkbox.setChecked(True)
    
    def get_indicator_data(self):
        """获取指标数据"""
        return {
            'selected_indicators': self.get_selected_indicators(),
            'financial_indicators': ['initial_investment', 'irr', 'dpp', 'npv', 'annual_maintenance', 'energy_purchase'],
            'technical_indicators': ['energy_supply_ratio', 'battery_utilization', 'hydrogen_utilization', 'equivalent_hours'],
            'environmental_indicators': ['renewable_ratio']
        }
    
    def load_indicator_data(self, data):
        """加载指标数据"""
        if data and 'selected_indicators' in data:
            self.set_selected_indicators(data['selected_indicators'])


# 测试代码
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    # 创建测试窗口
    window = IndicatorManagementPage()
    window.setWindowTitle("指标管理页面测试")
    window.resize(1000, 700)
    window.show()
    
    sys.exit(app.exec_())