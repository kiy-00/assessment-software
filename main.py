import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QListWidget, QStackedWidget,
                             QLabel, QFrame, QSizePolicy, QMessageBox, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from data_manager import DataManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data_manager = DataManager()
        self.project_design_page = None
        self.indicator_management_page = None
        self.load_icons()  # 添加图标加载
        self.init_ui()
    
    def load_icons(self):
        """加载图标资源"""
        self.icons = {}
        icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
        
        print(f"图标目录路径: {icons_dir}")  # 调试信息
        
        icon_files = {
            'new_project': '新建评估.svg',
            'open_project': '打开评估文件.svg',
            'project_design': '项目参数设计.svg',
            'indicator_management': '指标管理.svg',
            'evaluation': '综合评估.svg',
            'help': '查看帮助文档.svg'
        }
        
        for key, filename in icon_files.items():
            icon_path = os.path.join(icons_dir, filename)
            print(f"尝试加载图标: {icon_path}")  # 调试信息
            if os.path.exists(icon_path):
                self.icons[key] = QIcon(icon_path)
                print(f"成功加载图标: {key}")  # 调试信息
            else:
                self.icons[key] = QIcon()  # 空图标
                print(f"图标文件不存在: {icon_path}")  # 调试信息

    def init_ui(self):
        # 设置窗口基本属性
        self.setWindowTitle("可再生能源-氢能耦合项目技术经济性综合评估软件v1")
        self.setGeometry(100, 100, 1000, 700)
        
        # 设置窗口图标
        if 'evaluation' in self.icons and not self.icons['evaluation'].isNull():
            self.setWindowIcon(self.icons['evaluation'])
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # 创建顶部工具栏
        self.create_top_toolbar(main_layout)
        
        # 创建主内容区域
        self.create_main_content(main_layout)
        
        # 设置样式
        self.set_styles()
        
        # 创建状态栏
        self.statusBar()
    
    def create_top_toolbar(self, parent_layout):
        """创建顶部工具栏"""
        toolbar_frame = QFrame()
        toolbar_frame.setFrameStyle(QFrame.Box)
        toolbar_frame.setStyleSheet("QFrame { border: 1px solid #ddd; background-color: #f5f5f5; }")
        toolbar_frame.setMaximumHeight(80)
        
        toolbar_layout = QHBoxLayout(toolbar_frame)
        toolbar_layout.setSpacing(20)
        toolbar_layout.setContentsMargins(20, 15, 20, 15)
        
        # 新建评估按钮
        self.btn_new_evaluation = QPushButton("新建评估")
        if 'new_project' in self.icons and not self.icons['new_project'].isNull():
            self.btn_new_evaluation.setIcon(self.icons['new_project'])
        self.btn_new_evaluation.setMinimumSize(100, 50)
        self.btn_new_evaluation.clicked.connect(self.new_evaluation)
        
        # 打开评估文件按钮
        self.btn_open_file = QPushButton("打开评估文件")
        if 'open_project' in self.icons and not self.icons['open_project'].isNull():
            self.btn_open_file.setIcon(self.icons['open_project'])
        self.btn_open_file.setMinimumSize(100, 50)
        self.btn_open_file.clicked.connect(self.open_file)
        
        # 查看帮助文档按钮
        self.btn_help = QPushButton("查看帮助文档")
        if 'help' in self.icons and not self.icons['help'].isNull():
            self.btn_help.setIcon(self.icons['help'])
        self.btn_help.setMinimumSize(100, 50)
        self.btn_help.clicked.connect(self.show_help)
        
        # 添加按钮到布局
        toolbar_layout.addWidget(self.btn_new_evaluation)
        toolbar_layout.addWidget(self.btn_open_file)
        toolbar_layout.addWidget(self.btn_help)
        toolbar_layout.addStretch()  # 添加弹性空间
        
        parent_layout.addWidget(toolbar_frame)
    
    def create_main_content(self, parent_layout):
        """创建主内容区域"""
        content_layout = QHBoxLayout()
        content_layout.setSpacing(10)
        
        # 创建左侧导航栏
        self.create_left_navigation(content_layout)
        
        # 创建右侧内容区域
        self.create_right_content(content_layout)
        
        parent_layout.addLayout(content_layout)
    
    def create_left_navigation(self, parent_layout):
        """创建左侧导航栏"""
        nav_frame = QFrame()
        nav_frame.setFrameStyle(QFrame.Box)
        nav_frame.setStyleSheet("QFrame { border: 1px solid #ddd; background-color: #f9f9f9; }")
        nav_frame.setFixedWidth(200)
        
        nav_layout = QVBoxLayout(nav_frame)
        nav_layout.setContentsMargins(10, 20, 10, 20)
        nav_layout.setSpacing(15)
        
        # 导航标题
        nav_title = QLabel("功能导航")
        nav_title.setAlignment(Qt.AlignCenter)
        nav_title.setStyleSheet("QLabel { font-weight: bold; font-size: 20px; color: #333; }")
        nav_layout.addWidget(nav_title)
        
        # 导航按钮
        self.btn_project_design = QPushButton("项目参数设计")
        if 'project_design' in self.icons and not self.icons['project_design'].isNull():
            self.btn_project_design.setIcon(self.icons['project_design'])
        self.btn_project_design.setMinimumHeight(40)
        self.btn_project_design.clicked.connect(lambda: self.switch_content(0))
        
        self.btn_indicator_management = QPushButton("指标管理")
        if 'indicator_management' in self.icons and not self.icons['indicator_management'].isNull():
            self.btn_indicator_management.setIcon(self.icons['indicator_management'])
        self.btn_indicator_management.setMinimumHeight(40)
        self.btn_indicator_management.clicked.connect(lambda: self.switch_content(1))
        
        self.btn_comprehensive_evaluation = QPushButton("综合评估")
        if 'evaluation' in self.icons and not self.icons['evaluation'].isNull():
            self.btn_comprehensive_evaluation.setIcon(self.icons['evaluation'])
        self.btn_comprehensive_evaluation.setMinimumHeight(40)
        self.btn_comprehensive_evaluation.clicked.connect(lambda: self.switch_content(2))
        
        # 添加导航按钮
        nav_layout.addWidget(self.btn_project_design)
        nav_layout.addWidget(self.btn_indicator_management)
        nav_layout.addWidget(self.btn_comprehensive_evaluation)
        nav_layout.addStretch()  # 添加弹性空间
        
        parent_layout.addWidget(nav_frame)
    
    def create_right_content(self, parent_layout):
        """创建右侧内容区域"""
        # 创建堆叠部件用于切换不同页面
        self.stacked_widget = QStackedWidget()
        
        # 创建各个页面
        self.create_project_design_page()
        self.create_indicator_management_page()
        self.create_comprehensive_evaluation_page()
        
        parent_layout.addWidget(self.stacked_widget)
    
    def create_project_design_page(self):
        """创建项目参数设计页面"""
        from project_design_page import ProjectDesignPage
        
        self.project_design_page = ProjectDesignPage()
        
        # 连接数据更新信号
        self.project_design_page.data_updated.connect(self.on_project_data_updated)
        
        self.stacked_widget.addWidget(self.project_design_page)
        return self.project_design_page
    
    def create_indicator_management_page(self):
        """创建指标管理页面"""
        from indicator_management_page import IndicatorManagementPage
        
        self.indicator_management_page = IndicatorManagementPage()
        
        # 连接数据更新信号
        self.indicator_management_page.data_updated.connect(self.on_indicator_data_updated)
        
        self.stacked_widget.addWidget(self.indicator_management_page)
        return self.indicator_management_page
    
    def create_comprehensive_evaluation_page(self):
        """创建综合评估页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("综合评估")
        title.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; color: #2c3e50; }")
        layout.addWidget(title)
        
        content = QLabel("这里将显示综合评估的具体内容...")
        content.setStyleSheet("QLabel { font-size: 12px; color: #666; margin-top: 20px; }")
        layout.addWidget(content)
        
        layout.addStretch()
        self.stacked_widget.addWidget(page)
    
    def set_styles(self):
        """设置样式"""
        # 设置按钮样式
        button_style = """
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
        """
        
        # 应用样式到顶部按钮
        self.btn_new_evaluation.setStyleSheet(button_style)
        self.btn_open_file.setStyleSheet(button_style)
        self.btn_help.setStyleSheet(button_style)
        
        # 导航按钮样式
        nav_button_style = """
        QPushButton {
            background-color: #ecf0f1;
            color: #2c3e50;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            padding: 10px;
            font-size: 20px;
            text-align: left;
        }
        QPushButton:hover {
            background-color: #d5dbdb;
        }
        QPushButton:pressed {
            background-color: #aeb6bf;
        }
        """
        
        self.btn_project_design.setStyleSheet(nav_button_style)
        self.btn_indicator_management.setStyleSheet(nav_button_style)
        self.btn_comprehensive_evaluation.setStyleSheet(nav_button_style)
    
    def switch_content(self, index):
        """切换内容页面"""
        self.stacked_widget.setCurrentIndex(index)
    
    # 事件处理函数
    def new_evaluation(self):
        """新建评估"""
        project_path = self.data_manager.create_new_project(self)
        if project_path:
            QMessageBox.information(self, "成功", f"项目创建成功！\n项目路径：{project_path}")
            
            # 重置项目参数设计页面并设置默认值
            if self.project_design_page:
                self.project_design_page.reset_form()
            
            # 重置指标管理页面
            if self.indicator_management_page:
                self.indicator_management_page.set_selected_indicators([
                    'initial_investment', 'irr', 'dpp', 'npv', 
                    'annual_maintenance', 'energy_purchase',
                    'battery_utilization', 'hydrogen_utilization',
                    'renewable_ratio'
                ])
            
            # 立即保存默认数据
            self.save_default_data()
    
    def save_default_data(self):
        """保存默认数据"""
        if self.project_design_page and self.data_manager.current_project_path:
            project_data = self.project_design_page.get_project_data()
            
            # 获取指标数据
            indicator_data = {'selected_indicators': []}
            if self.indicator_management_page:
                indicator_data = self.indicator_management_page.get_indicator_data()
            
            # 保存数据
            if self.data_manager.save_project_data(project_data, indicator_data):
                self.statusBar().showMessage("默认数据已保存", 2000)
    
    def open_file(self):
        """打开评估文件"""
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "选择项目文件夹",
            os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        
        if folder_path:
            # 检查是否是有效的项目文件夹
            if os.path.exists(os.path.join(folder_path, "User_input.json")) and \
               os.path.exists(os.path.join(folder_path, "IndicatorSystem.json")):
                
                if self.data_manager.load_project(folder_path):
                    # 加载数据到UI
                    project_data = self.data_manager.get_project_data_for_ui()
                    indicator_data = self.data_manager.get_indicator_data_for_ui()
                    
                    if self.project_design_page:
                        self.project_design_page.load_project_data(project_data)
                    
                    if self.indicator_management_page:
                        self.indicator_management_page.load_indicator_data(indicator_data)
                    
                    QMessageBox.information(self, "成功", "项目加载成功！")
                else:
                    QMessageBox.warning(self, "错误", "加载项目失败！")
            else:
                QMessageBox.warning(self, "错误", "选择的文件夹不是有效的项目文件夹！")
    
    def show_help(self):
        """查看帮助文档"""
        help_text = "可再生能源-氢能耦合项目技术经济性综合评估软件v1\n\n使用说明：\n1. 点击\"新建评估\"创建新项目\n2. 在\"项目参数设计\"中填写项目参数\n3. 在\"指标管理\"中选择评估指标\n4. 在\"综合评估\"中查看评估结果"
        QMessageBox.information(self, "帮助", help_text)
    
    def on_project_data_updated(self):
        """项目数据更新处理"""
        print("项目参数数据已更新")
        
        # 获取项目参数数据
        if self.project_design_page and self.data_manager.current_project_path:
            project_data = self.project_design_page.get_project_data()
            
            # 获取指标数据
            indicator_data = {'selected_indicators': []}
            if self.indicator_management_page:
                indicator_data = self.indicator_management_page.get_indicator_data()
            
            # 保存数据
            if self.data_manager.save_project_data(project_data, indicator_data):
                self.statusBar().showMessage("数据已保存", 2000)
            else:
                self.statusBar().showMessage("数据保存失败", 2000)
    
    def on_indicator_data_updated(self):
        """指标数据更新处理"""
        print("指标管理数据已更新")
        
        # 获取指标数据
        if self.indicator_management_page and self.data_manager.current_project_path:
            indicator_data = self.indicator_management_page.get_indicator_data()
            
            # 获取项目参数数据
            project_data = {}
            if self.project_design_page:
                project_data = self.project_design_page.get_project_data()
            
            # 保存数据
            if self.data_manager.save_project_data(project_data, indicator_data):
                self.statusBar().showMessage("指标数据已保存", 2000)
            else:
                self.statusBar().showMessage("指标数据保存失败", 2000)

def main():
    # 设置DPI感知，解决不同缩放比例下字体大小不一致的问题
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 设置现代化风格
    
    # 设置全局字体
    font = QFont("微软雅黑", 9)  # 统一字体大小
    app.setFont(font)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()