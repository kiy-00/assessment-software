import sys
import os
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QFrame, QScrollArea, QTextEdit,
                             QProgressBar, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

class ComprehensiveEvaluationPage(QWidget):
    """综合评估页面"""
    
    evaluation_started = pyqtSignal()  # 评估开始信号
    
    def __init__(self):
        super().__init__()
        self.load_icons()
        self.init_ui()
    
    def load_icons(self):
        """加载图标资源"""
        self.icons = {}
        icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
        
        print(f"综合评估页面 - 图标目录路径: {icons_dir}")  # 调试信息
        
        icon_files = {
            'evaluation': '综合评估.svg'
        }
        
        for key, filename in icon_files.items():
            icon_path = os.path.join(icons_dir, filename)
            print(f"综合评估页面 - 尝试加载图标: {icon_path}")  # 调试信息
            if os.path.exists(icon_path):
                self.icons[key] = QIcon(icon_path)
                print(f"综合评估页面 - 成功加载图标: {key}")  # 调试信息
            else:
                self.icons[key] = QIcon()
                print(f"综合评估页面 - 图标文件不存在: {icon_path}")  # 调试信息

    def init_ui(self):
        """初始化用户界面"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # 页面标题
        title = QLabel("综合评估")
        title.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; color: #2c3e50; }")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # 创建控制按钮区域
        self.create_control_buttons(main_layout)
        
        # 创建结果显示区域
        self.create_results_area(main_layout)
    
    def create_control_buttons(self, parent_layout):
        """创建控制按钮"""
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        # 开始评估按钮组合
        eval_layout = QHBoxLayout()
        eval_layout.setSpacing(8)
        
        # 添加图标
        if 'evaluation' in self.icons and not self.icons['evaluation'].isNull():
            eval_icon = QLabel()
            eval_icon.setPixmap(self.icons['evaluation'].pixmap(24, 24))
            eval_icon.setAlignment(Qt.AlignCenter)
            eval_icon.setStyleSheet("QLabel { border: none; background: transparent; }")  # 去掉边框和背景
            eval_layout.addWidget(eval_icon)
            print("综合评估页面 - 已设置按钮图标")  # 调试信息
        else:
            print("综合评估页面 - 图标为空，未设置按钮图标")  # 调试信息
        
        # 开始评估按钮
        self.start_btn = QPushButton("开始评估")
        self.start_btn.setMinimumSize(120, 35)
        self.start_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 9pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #219a52;
            }
            QPushButton:pressed {
                background-color: #1e8449;
            }
        """)
        self.start_btn.clicked.connect(self.start_evaluation)
        eval_layout.addWidget(self.start_btn)
        
        button_layout.addLayout(eval_layout)
        parent_layout.addLayout(button_layout)
    
    def create_results_area(self, parent_layout):
        """创建结果显示区域"""
        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        # 结果内容
        results_widget = QWidget()
        results_layout = QVBoxLayout(results_widget)
        
        # 评估进度
        progress_label = QLabel("评估进度：")
        progress_label.setStyleSheet("QLabel { font-size: 12px; font-weight: bold; }")
        results_layout.addWidget(progress_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        results_layout.addWidget(self.progress_bar)
        
        # 评估结果
        result_label = QLabel("评估结果：")
        result_label.setStyleSheet("QLabel { font-size: 12px; font-weight: bold; margin-top: 20px; }")
        results_layout.addWidget(result_label)
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlainText("请先完成项目参数设计和指标选择，然后点击\"开始评估\"按钮进行综合评估。")
        results_layout.addWidget(self.result_text)
        
        scroll_area.setWidget(results_widget)
        parent_layout.addWidget(scroll_area)
    
    def start_evaluation(self):
        """开始评估"""
        print("开始综合评估...")
        
        # 显示进度条
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # 更新结果文本
        self.result_text.setPlainText("正在进行综合评估，请稍候...")
        
        # 发出评估开始信号
        self.evaluation_started.emit()
        
        # 这里可以添加实际的评估逻辑
        # 暂时模拟评估过程
        self.simulate_evaluation()
    
    def simulate_evaluation(self):
        """模拟评估过程"""
        import time
        from PyQt5.QtCore import QTimer
        
        self.timer = QTimer()
        self.progress_value = 0
        
        def update_progress():
            self.progress_value += 10
            self.progress_bar.setValue(self.progress_value)
            
            if self.progress_value >= 100:
                self.timer.stop()
                self.show_evaluation_results()
        
        self.timer.timeout.connect(update_progress)
        self.timer.start(200)  # 每200ms更新一次
    
    def show_evaluation_results(self):
        """显示评估结果"""
        result_text = """
综合评估完成！

评估结果摘要：
================

财务效益指标：
- 净现值(NPV): 1234.56万元
- 内部收益率(IRR): 12.5%
- 投资回收期(DPP): 8.2年

技术效益指标：
- 电储能利用水平: 85%
- 氢储能利用水平: 78%

环境效益指标：
- 可再生能源供应占比: 92%

综合评估得分: 85.6分

建议：
该项目在技术经济性方面表现良好，建议进一步优化储能配置以提高整体效率。
        """
        
        self.result_text.setPlainText(result_text)
        self.progress_bar.setVisible(False)


# 测试代码
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    # 创建测试窗口
    window = ComprehensiveEvaluationPage()
    window.setWindowTitle("综合评估页面测试")
    window.resize(800, 600)
    window.show()
    
    sys.exit(app.exec_())
