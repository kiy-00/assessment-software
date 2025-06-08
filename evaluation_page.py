import os
from PyQt5.QtWidgets import QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class EvaluationPage:
    def __init__(self):
        super().__init__()
        self.load_icons()
        self.init_ui()
        self.setup_connections()
    
    def load_icons(self):
        """加载图标资源"""
        self.icons = {}
        icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
        
        icon_files = {
            'evaluation': '综合评估.svg'
        }
        
        for key, filename in icon_files.items():
            icon_path = os.path.join(icons_dir, filename)
            if os.path.exists(icon_path):
                self.icons[key] = QIcon(icon_path)
            else:
                self.icons[key] = QIcon()

    def create_control_buttons(self, parent_layout):
        """创建控制按钮"""
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        # 开始评估按钮
        self.start_btn = QPushButton("开始评估")
        if 'evaluation' in self.icons:
            self.start_btn.setIcon(self.icons['evaluation'])
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
        
        button_layout.addWidget(self.start_btn)
        parent_layout.addLayout(button_layout)