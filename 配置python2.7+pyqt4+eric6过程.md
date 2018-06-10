## 本项目是基于python2.7+pyqt4+eric6环境的，配置过程如下

## 工具准备
  （1）sip-4.17
  （2）QScintilla-gpl-2.9.1
  （3）PyQt-x11-gpl-4.11.4
  （4）eric6-17.12
  （5）eric6-i18n-zh_CN-17.12
## 配置过程
### 一、SIP安装
  因为系统接口都是C, C++的而python要调用这些C/C++接口，就需要这个SIP，安装PyQt之前必须先安装对应版本的SIP。PyQt编译时使用的SIP版本必须与python默认调用的SIP保持一致！否则python中是无法调用PyQt的。在安装sip之前，要先查看一下python2.7中sip版本:<br>
  
    import sip
    print sip.SIP_VERSION_STR
   发现python2.7中是4.17，所有我这里安装4.17版本的。<br>
      
    cd sip-4.17 
    python configure.py  
    sudo make  
    sudo make install 
   安装完后，终端核实一下：<br>
    
    sip -V
   发现也是4.17，SIP安装完毕。
 ### 二、QScintilla安装
  QScintilla2是连接编译器和Python的接口，是Eric的必需前置组件。QScintilla2 中需要单独安装3个模块，本体，Designer和python bindings。这一步先只安装本体部分，后面两个需要等安装了PyQt4才能安装，这个顺序不能搞错，不然会在安装QScintilla的python bindings时会无法生成C++ code，导致安装的失败。
  #### 安装本体：
    cd QScintilla-gpl-2.9.1
    cd Qt4Qt5  
    qmake-qt4 qscintilla.pro  
    sudo make  
    sudo make install
 ### 三、安装PyQT4
  PyQt是Python的一个跨平台图形开发工具集，是Python与Qt的成功融合。PyQt包含了大约440个类、超过6000个的函数和方法。
  
    cd PyQt-gpl-5.7  
    sudo python configure.py --qmake /usr/bin/qmake-qt4 #需要指定qt4编译器
    sudo make
    sudo make install
 ### 四、安装QScintilla后续部分
  前面已经安装了本体Qt4Qt5部分了，这里在安装完PyQt4后，再继续安装后面的两个部分。
  #### 安装Designer
    cd QScintilla-gpl-2.9.1/designer-Qt4Qt5  
    qmake-qt4 designer.pro   
    sudo make  
    sudo make install
  #### 安装Python bindings(很重要)
    cd QScintilla-gpl-2.9.3/Python  
    sudo python configure.py --destdir=/usr/lib/python2.7/dist-packages/PyQt4 --pyqt=PyQt4 --pyqt-sipdir=/usr/share/sip/PyQt4 --qsci-incdir=/usr/include/qt4  --qsci-sipdir=/usr/share/sip/PyQt4  
    sudo make  
    sudo make install
   至此，基本环境就搭建完了，下面安装eric6。
 ### 五、安装eric6
  Eric是一款强大的开源Python IDE，支持Qt界面设计器的Eric在Python GUI开发中更是首屈一指，Python+PyQt+Eric已经成为一种标准的Python GUI开发平台。这里我们需要解压得到eric6-17.12和eric6-i18n-zh_CN-17.12两个安装包<br>
    
    cd eric6-17.12 
    sudo python install.py           //安装主程序  
    sudo python install-i18n.py   //安装中文语言包
   安装完成后，我们必须用sudo eric6打开，此时会发现在eric6里面无法切换中文输入法，此时我们进入终端对eric6赋予管理员权限
   
     sudo chmod a+w -R ~/.eric6
     sudo chmod a+w -R ~/.config/Eric6
   此时就可以直接在终端输入：eric6，打开编辑器，但此时我们会发现无法进行读写操作，继续赋予权限
   
     sudo chmod 777 -R ~/.eric6/eric6session.e5s
     sudo chmod 777 -R ~/.eric6/eric6tasks.e6t
   
 ### 至此可正常使用eric6。一切环境搭建完成。
   
    
   
 
