import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QListWidget, QStackedWidget,
                             QLabel, QFrame, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

from utils import ProjectArgsReader
from DataStructure import ProjectArgs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.__data_folder = "./v2"

    def init_ui(self):
        # 设置窗口基本属性
        self.setWindowTitle("可再生能源-氢能耦合项目技术经济性综合评估软件v1")
        self.setGeometry(100, 100, 1000, 700)

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
        self.btn_new_evaluation.setMinimumSize(100, 50)
        self.btn_new_evaluation.clicked.connect(self.new_evaluation)

        # 打开评估文件按钮
        self.btn_open_file = QPushButton("打开评估文件")
        self.btn_open_file.setMinimumSize(100, 50)
        self.btn_open_file.clicked.connect(self.open_file)

        # 查看帮助文档按钮
        self.btn_help = QPushButton("查看帮助文档")
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
        self.btn_project_design.setMinimumHeight(40)
        self.btn_project_design.clicked.connect(lambda: self.switch_content(0))

        self.btn_indicator_management = QPushButton("指标管理")
        self.btn_indicator_management.setMinimumHeight(40)
        self.btn_indicator_management.clicked.connect(lambda: self.switch_content(1))

        self.btn_comprehensive_evaluation = QPushButton("综合评估")
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

        page = ProjectDesignPage()

        # 连接数据更新信号
        page.data_updated.connect(self.on_project_data_updated)

        self.stacked_widget.addWidget(page)
        return page

    def create_indicator_management_page(self):
        """创建指标管理页面"""
        from indicator_management_page import IndicatorManagementPage

        page = IndicatorManagementPage()

        # 连接数据更新信号
        page.data_updated.connect(self.on_indicator_data_updated)

        self.stacked_widget.addWidget(page)
        return page

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
        print("新建评估")

    def open_file(self):
        print("打开评估文件")
        self.handle_open_file()

    def show_help(self):
        print("查看帮助文档")

    def on_project_data_updated(self):
        """项目数据更新处理"""
        print("项目参数数据已更新")

    def on_indicator_data_updated(self):
        """指标数据更新处理"""
        print("指标管理数据已更新")

    def handle_open_file(self):
        project_args_reader = ProjectArgsReader(self.__data_folder)


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 设置现代化风格

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
