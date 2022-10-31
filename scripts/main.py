#!/usr/bin/python3
# coding=utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from login import Ui_MainWindow as LoginWindow
from check import Ui_Form as CheckWindow
from controlUI import Ui_Form as ControlWindow
import rospy
from std_msgs.msg import String, Int64
from electroplate_ui_git.srv import *


class MyLoginWindow(QtWidgets.QMainWindow, LoginWindow):
    def __init__(self, parent=None):
        super(MyLoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.load_all_static_pics()
        self.connect_signals_slots()

    def load_all_static_pics(self):
        self.label.setPixmap(QtGui.QPixmap("/home/diandu/catkin_ws/src/electroplate_ui_git/scripts/hangyi.png"))
        self.label_2.setPixmap(QtGui.QPixmap("/home/diandu/catkin_ws/src/electroplate_ui_git/scripts//robotlab.png"))

    def connect_signals_slots(self):
        # self.connect_db_signal.connect(self.print_text)
        self.pushButton.clicked.connect(self.word_get)

    def word_get(self):
        # global id
        # global login_id
        login_user = self.lineEdit.text()
        print(login_user)
        login_password = self.lineEdit_2.text()
        if login_user == '5720' and login_password == '5720':
            MyCheck.show()
            MyControl.update_time('label_login_time')
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self,
                                          "警告",
                                          "用户名或密码错误！",
                                          QtWidgets.QMessageBox.Yes)


class MyCheckWindow(QtWidgets.QMainWindow, CheckWindow):
    check_id = True

    def __init__(self, parent=None):
        super(MyCheckWindow, self).__init__(parent)
        self.setupUi(self)
        self.load_all_static_pics()
        self.connect_signals_slots()

    def load_all_static_pics(self):
        self.label.setPixmap(QtGui.QPixmap("/home/diandu/catkin_ws/src/electroplate_ui_git/scripts//hangyi.png"))
        self.label_2.setPixmap(QtGui.QPixmap("/home/diandu/catkin_ws/src/electroplate_ui_git/scripts//robotlab.png"))

    def connect_signals_slots(self):
        # self.connect_db_signal.connect(self.print_text)
        self.pushButton.clicked.connect(gui_node.first_check)
        self.pushButton_2.clicked.connect(self.start_control)

    def check_status(self):
        # 检查rosparam
        self.check_id = True

    def start_control(self):
        if self.check_id:
            MyControl.show()
            self.close()


class MyControlWindow(QtWidgets.QMainWindow, ControlWindow):
    def __init__(self, parent=None):
        super(MyControlWindow, self).__init__(parent)
        self.setupUi(self)
        self.load_all_static_pics()
        self.init_signal_light()
        self.connect_signals_slots()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label_status)
        self.timer.start(1000)

    def load_all_static_pics(self):
        self.label.setPixmap(QtGui.QPixmap("/home/diandu/catkin_ws/src/electroplate_ui_git/scripts//hangyi.png"))
        self.label_2.setPixmap(QtGui.QPixmap("/home/diandu/catkin_ws/src/electroplate_ui_git/scripts//robotlab.png"))

    def connect_signals_slots(self):
        # self.connect_db_signal.connect(self.print_text)
        self.workStartButton.clicked.connect(gui_node.work_start)
        self.workEndButton.clicked.connect(gui_node.work_end)

    def init_signal_light(self):
        self.label_change_color('label_robot1_status', 'init')
        self.label_change_color('label_robot2_status', 'init')
        self.label_change_color('label_pot_status', 'init')
        self.label_change_color('label_plc_status', 'init')
        self.label_change_color('label_database_status', 'init')
        self.label_change_color('label_raster1_status', 'init')
        self.label_change_color('label_raster2_status', 'init')
        self.label_change_color('label_raster3_status', 'init')
        self.label_change_color('label_raster4_status', 'init')
        self.label_change_color('label_radar11_status', 'init')
        self.label_change_color('label_radar12_status', 'init')
        self.label_change_color('label_radar21_status', 'init')
        self.label_change_color('label_radar22_status', 'init')
        self.label_change_color('label_laser11_status', 'init')
        self.label_change_color('label_laser12_status', 'init')
        self.label_change_color('label_laser21_status', 'init')
        self.label_change_color('label_emergency_status', 'init')
        self.label_change_color('label_whole_status', 'init')

    def update_label_status(self):
        flag = rospy.get_param("/params//robot0/connection_status")
        if flag:
            self.label_change_color('label_robot1_status', 'green')
        else:
            self.label_change_color('label_robot1_status', 'red')

        flag = rospy.get_param("/params//robot1/connection_status")
        if flag:
            self.label_change_color('label_robot2_status', 'green')
        else:
            self.label_change_color('label_robot2_status', 'red')

        flag = rospy.get_param("/params//plc_connection_status")
        if flag:
            self.label_change_color('label_plc_status', 'green')
        else:
            self.label_change_color('label_plc_status', 'red')

        flag = rospy.get_param("/params//pot_connection_status")
        if flag:
            self.label_change_color('label_pot_status', 'green')
        else:
            self.label_change_color('label_pot_status', 'red')

        flag = rospy.get_param("/params//database_connection_status")
        if flag:
            self.label_change_color('label_database_status', 'green')
        else:
            self.label_change_color('label_database_status', 'red')

        flag = rospy.get_param("/params/raster1_status")
        if flag:
            self.label_change_color('label_raster1_status', 'green')
        else:
            self.label_change_color('label_raster1_status', 'red')

        flag = rospy.get_param("/params/raster2_status")
        if flag:
            self.label_change_color('label_raster2_status', 'green')
        else:
            self.label_change_color('label_raster2_status', 'red')

        flag = rospy.get_param("/params/raster3_status")
        if flag:
            self.label_change_color('label_raster3_status', 'green')
        else:
            self.label_change_color('label_raster3_status', 'red')

        flag = rospy.get_param("/params/raster4_status")
        if flag:
            self.label_change_color('label_raster4_status', 'green')
        else:
            self.label_change_color('label_raster4_status', 'red')

        flag = rospy.get_param("/params/robot0/radar1_status")
        if flag:
            self.label_change_color('label_radar11_status', 'green')
        else:
            self.label_change_color('label_radar11_status', 'red')

        flag = rospy.get_param("/params/robot0/radar2_status")
        if flag:
            self.label_change_color('label_radar12_status', 'green')
        else:
            self.label_change_color('label_radar12_status', 'red')

        flag = rospy.get_param("/params/robot1/radar1_status")
        if flag:
            self.label_change_color('label_radar21_status', 'green')
        else:
            self.label_change_color('label_radar21_status', 'red')

        flag = rospy.get_param("/params/robot1/radar2_status")
        if flag:
            self.label_change_color('label_radar22_status', 'green')
        else:
            self.label_change_color('label_radar22_status', 'red')

        flag = rospy.get_param("/params/robot0/laser1_status")
        if flag:
            self.label_change_color('label_laser11_status', 'green')
        else:
            self.label_change_color('label_laser11_status', 'red')

        flag = rospy.get_param("/params/robot0/laser2_status")
        if flag:
            self.label_change_color('label_laser12_status', 'green')
        else:
            self.label_change_color('label_laser12_status', 'red')

        flag = rospy.get_param("/params/robot1/laser1_status")
        if flag:
            self.label_change_color('label_laser21_status', 'green')
        else:
            self.label_change_color('label_laser21_status', 'red')

        flag = rospy.get_param("/params/emergency_status")
        if flag:
            self.label_change_color('label_emergency_status', 'green')
        else:
            self.label_change_color('label_emergency_status', 'red')

        flag = rospy.get_param("/params/system_whole_status")
        if flag:
            self.label_change_color('label_whole_status', 'green')
        else:
            self.label_change_color('label_whole_status', 'red')

    def label_change_color(self, label_name, status='init'):
        """
        :param label_name: label的objectName
        :param status: 状态：[初始，绿灯，红灯]
        :return:
        """
        color = {
            'init': '#0B610B', 'green': '#9ACD32', 'red': '#FF4000'}[status]
        style = """min-width: 20px; 
                   min-height: 20px;
                   max-width: 20px; 
                   max-height: 20px;
                   border-radius: 0px;  
                   border:1px solid black;
                   background:{};
                   font-size:14px;
                   color:white
                """.format(color)
        self.__getattribute__(label_name).setStyleSheet(style)  # 相当于 self.color_label.setStyleSheet(style)

    def update_time(self, label_name):
        time = QtCore.QDateTime.currentDateTime()  # 获取现在的时间
        timeplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')  # 设置显示时间的格式
        self.__getattribute__(label_name).setText(timeplay)  # 设置timeLabel控件显示的内容


class RosPyGUI:
    def __init__(self):
        # super(RosPyGUI, self).__init__(parent)
        rospy.init_node('RosPyGUI')
        print('ros is ok')
        # 开始与结束生产服务

        # self.pub = rospy.Publisher("/test_topic_for_GUI", Int64, queue_size=10)
        # self.number_subscriber = rospy.Subscriber("/number", Int64, self.callback_count)
        print('RosPyGUI inited.')

    def work_start(self):
        # 等待接入服务节点
        # 第二句是调用wait_for_service，阻塞直到名为“add_two_ints”的服务可用。
        flag = QtWidgets.QMessageBox.question(MyControl, "确认", "是否确定开启生产？",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if flag==QtWidgets.QMessageBox.Yes:
            rospy.wait_for_service('workStartEnd')
            # 创建服务的处理句柄,可以像调用函数一样，调用句柄
            work_start = rospy.ServiceProxy('workStartEnd', workStartEnd)
            resp = work_start(True, False)
            if resp.work_start_check_flag:
                QtWidgets.QMessageBox.warning(MyControl,
                                              "通知",
                                              "开启生产成功，请执行上下料！",
                                              QtWidgets.QMessageBox.Yes)
            else:
                QtWidgets.QMessageBox.warning(MyControl,
                                              "警告",
                                              "生产已开启，勿重复点击！",
                                              QtWidgets.QMessageBox.Yes)

    def work_end(self):
        # 等待接入服务节点
        # 第二句是调用wait_for_service，阻塞直到名为“add_two_ints”的服务可用。
        flag = QtWidgets.QMessageBox.question(MyControl, "确认", "是否确定结束生产？",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if flag == QtWidgets.QMessageBox.Yes:
            rospy.wait_for_service('workStartEnd')
            # 创建服务的处理句柄,可以像调用函数一样，调用句柄
            work_end = rospy.ServiceProxy('workStartEnd', workStartEnd)
            resp = work_end(False, True)
            if resp.work_end_check_flag:
                QtWidgets.QMessageBox.warning(MyControl,
                                              "通知",
                                              "结束生产成功，请取出上下料区推车！",
                                              QtWidgets.QMessageBox.Yes)
            else:
                QtWidgets.QMessageBox.warning(MyControl,
                                              "警告",
                                              "当前生产未结束，请在当前生产任务结束后点击！",
                                              QtWidgets.QMessageBox.Yes)

    def first_check(self):
        MyCheck.textBrowser.setPlainText('')
        flag = True
        connection_robot0 = rospy.get_param("/params/robot0/connection_status")
        if connection_robot0:
            text = "1号机械臂模块已连接！\n"
        else:
            text = "1号机械臂模块未连接！\n"
            flag = False
        MyCheck.textBrowser.append(text)

        connection_robot1 = rospy.get_param("/params/robot1/connection_status")
        if connection_robot1:
            text = "2号机械臂模块已连接！\n"
        else:
            text = "2号机械臂模块未连接！\n"
            flag = False
        MyCheck.textBrowser.append(text)

        connection_plc = rospy.get_param("/params/plc_connection_status")
        if connection_plc:
            text = "plc模块已连接！\n"
        else:
            text = "plc模块未连接！\n"
            flag = False
        MyCheck.textBrowser.append(text)

        connection_pot = rospy.get_param("/params/pot_connection_status")
        if connection_pot:
            text = "电镀槽模块已连接！\n"
        else:
            text = "电镀槽模块未连接！\n"
            flag = False
        MyCheck.textBrowser.append(text)

        connection_database = rospy.get_param("/params/database_connection_status")
        if connection_database:
            text = "数据库模块已连接！\n"
        else:
            text = "数据库模块未连接！\n"
            flag = False
        MyCheck.textBrowser.append(text)

        if flag:
            text = "可以进入生产界面！ \n"
        else:
            text = "请检查产线各模块连接情况！ \n"
        MyCheck.textBrowser.append(text)


if __name__ == "__main__":
    # rospy.init_node('RosPyGUI')
    # print('ros is ok')
    # print('RosPyGUI inited.')
    gui_node = RosPyGUI()
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    # MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    # ui = Ui_MainWindow()                    # ui是Ui_MainWindow()类的实例化对象
    # ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    # MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    # sys.exit(app.exec_())
    MyCheck = MyCheckWindow()
    MyControl = MyControlWindow()
    MyLogin = MyLoginWindow()
    MyLogin.show()
    # MyLogin.pushButton.clicked.connect(MyLogin.close)
    # MyLogin.pushButton.clicked.connect(MyCheck.show)
    sys.exit(app.exec_())
