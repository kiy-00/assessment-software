import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QTabWidget, QMenuBar, QStatusBar, QAction, 
                             QMessageBox, QFileDialog, QSplitter)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

from project_design_page import ProjectDesignPage
from indicator_management_page import IndicatorManagementPage
from evaluation_page import EvaluationPage
from data_manager import DataManager

class MainWindow(QMainWindow):
    """主窗口类"""
    
    def __init__(self):
        super().__init__()
        self.data_manager = DataManager()
        self.current_project_path = None
        self.init_ui()
        self.setup_connections()
        self.load_icons()
    
    def load_icons(self):
        """加载图标资源"""
        self.icons = {}
        icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
        
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
            if os.path.exists(icon_path):
                self.icons[key] = QIcon(icon_path)
            else:
                self.icons[key] = QIcon()  # 空图标
    
    def init_ui(self):
        """初始化用户界面"""
        self.setWindowTitle("综合能源系统经济性评估软件")
        self.setGeometry(100, 100, 1400, 900)
        
        # 设置应用程序图标
        if 'evaluation' in self.icons:
            self.setWindowIcon(self.icons['evaluation'])
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建选项卡窗口
        self.create_tab_widget()
        main_layout.addWidget(self.tab_widget)
        
        # 创建状态栏
        self.create_status_bar()
        
        # 设置样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QTabWidget::pane {
                border: 1px solid #c0c0c0;
                background-color: white;
            }
            QTabWidget::tab-bar {
                alignment: left;
            }
            QTabBar::tab {
                background-color: #e1e1e1;
                border: 1px solid #c0c0c0;
                padding: 8px 20px;
                margin-right: 2px;
                border-bottom: none;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom: 1px solid white;
            }
            QTabBar::tab:hover {
                background-color: #f0f0f0;
            }
        """)

    def create_menu_bar(self):
        """创建菜单栏"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu('文件(&F)')
        
        # 新建项目
        new_action = QAction('新建评估项目(&N)', self)
        if 'new_project' in self.icons:
            new_action.setIcon(self.icons['new_project'])
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('创建新的评估项目')
        new_action.triggered.connect(self.new_project)
        file_menu.addAction(new_action)
        
        # 打开项目
        open_action = QAction('打开评估项目(&O)', self)
        if 'open_project' in self.icons:
            open_action.setIcon(self.icons['open_project'])
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('打开现有的评估项目')
        open_action.triggered.connect(self.open_project)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        # 退出
        exit_action = QAction('退出(&X)', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('退出应用程序')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 帮助菜单
        help_menu = menubar.addMenu('帮助(&H)')
        
        # 帮助文档
        help_action = QAction('查看帮助文档(&H)', self)
        if 'help' in self.icons:
            help_action.setIcon(self.icons['help'])
        help_action.setShortcut('F1')
        help_action.setStatusTip('查看帮助文档')
        help_action.triggered.connect(self.show_help)
        help_menu.addAction(help_action)
        
        # 关于
        about_action = QAction('关于(&A)', self)
        about_action.setStatusTip('关于本软件')
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def create_tab_widget(self):
        """创建选项卡窗口"""
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.North)
        
        # 创建各个页面
        self.project_design_page = ProjectDesignPage()
        self.indicator_management_page = IndicatorManagementPage()
        self.evaluation_page = EvaluationPage()
        
        # 添加选项卡并设置图标
        tab_index = self.tab_widget.addTab(self.project_design_page, "项目参数设计")
        if 'project_design' in self.icons:
            self.tab_widget.setTabIcon(tab_index, self.icons['project_design'])
        
        tab_index = self.tab_widget.addTab(self.indicator_management_page, "指标管理")
        if 'indicator_management' in self.icons:
            self.tab_widget.setTabIcon(tab_index, self.icons['indicator_management'])
        
        tab_index = self.tab_widget.addTab(self.evaluation_page, "综合评估")
        if 'evaluation' in self.icons:
            self.tab_widget.setTabIcon(tab_index, self.icons['evaluation'])

    def create_status_bar(self):
        """创建状态栏"""
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("准备就绪")

    # ...existing code...