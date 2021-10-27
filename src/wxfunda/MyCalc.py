'''
Created on 2021. 7. 21.

@author: pc358
'''
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 280,558 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        self.SetBackgroundColour( wx.Colour( 255, 220, 191 ) )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.txt_res = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,50 ), 0 )
        bSizer2.Add( self.txt_res, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
        
        gSizer2 = wx.GridSizer( 7, 4, 5, 5 )
        
        self.m_button99 = wx.Button( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.Size( 30,30 ), 0|wx.NO_BORDER )
        self.m_button99.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button99, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button10 = wx.Button( self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button10, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button11 = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button11, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button12 = wx.Button( self, wx.ID_ANY, u"DEL", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button12.SetBackgroundColour( wx.Colour( 255, 255, 183 ) )
        
        gSizer2.Add( self.m_button12, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button13 = wx.Button( self, wx.ID_ANY, u"1/x", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button13, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button14 = wx.Button( self, wx.ID_ANY, u"x²", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button14, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button15 = wx.Button( self, wx.ID_ANY, u"²√x", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button15, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button16 = wx.Button( self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button16, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button17 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button17.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button17, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button18 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button18, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button19 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button19, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button20 = wx.Button( self, wx.ID_ANY, u"×", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button20, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button21 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button21, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button22 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button22, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button23 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button23.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button23.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button23, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button24 = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button24.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button24, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button25 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button25.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button25.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button25, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button26 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button26.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button26.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button26, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button27 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button27.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button27.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button27, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button28 = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button28.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button28, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button29 = wx.Button( self, wx.ID_ANY, u"+/-", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button29.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button29, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button30 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        
        gSizer2.Add( self.m_button30, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button31 = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button31, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button32 = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button32.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        
        gSizer2.Add( self.m_button32, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button40 = wx.Button( self, wx.ID_ANY, u"(", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button40.SetBackgroundColour( wx.Colour( 255, 255, 240 ) )
        
        gSizer2.Add( self.m_button40, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button41 = wx.Button( self, wx.ID_ANY, u")", wx.DefaultPosition, wx.Size( 50,50 ), 0|wx.NO_BORDER )
        self.m_button41.SetBackgroundColour( wx.Colour( 255, 255, 240 ) )
        
        gSizer2.Add( self.m_button41, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer2.Add( gSizer2, 1, wx.ALIGN_CENTER, 5 )
        
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button99.Bind( wx.EVT_BUTTON, self.btnPer )
        self.m_button10.Bind( wx.EVT_BUTTON, self.btnClear )
        self.m_button11.Bind( wx.EVT_BUTTON, self.btnAllClear )
        self.m_button12.Bind( wx.EVT_BUTTON, self.btnDelete )
        self.m_button13.Bind( wx.EVT_BUTTON, self.btnDivideX )
        self.m_button14.Bind( wx.EVT_BUTTON, self.btnSqrX )
        self.m_button15.Bind( wx.EVT_BUTTON, self.btnRootX )
        self.m_button16.Bind( wx.EVT_BUTTON, self.btnDivide )
        self.m_button17.Bind( wx.EVT_BUTTON, self.btnSeven )
        self.m_button18.Bind( wx.EVT_BUTTON, self.btnEight )
        self.m_button19.Bind( wx.EVT_BUTTON, self.btnNine )
        self.m_button20.Bind( wx.EVT_BUTTON, self.btnMultiply )
        self.m_button21.Bind( wx.EVT_BUTTON, self.btnFour )
        self.m_button22.Bind( wx.EVT_BUTTON, self.btnFive )
        self.m_button23.Bind( wx.EVT_BUTTON, self.btnSIx )
        self.m_button24.Bind( wx.EVT_BUTTON, self.btnMinus )
        self.m_button25.Bind( wx.EVT_BUTTON, self.btnOne )
        self.m_button26.Bind( wx.EVT_BUTTON, self.btnTwo )
        self.m_button27.Bind( wx.EVT_BUTTON, self.btnThree )
        self.m_button28.Bind( wx.EVT_BUTTON, self.btnPlus )
        self.m_button29.Bind( wx.EVT_BUTTON, self.btnPosiNega )
        self.m_button30.Bind( wx.EVT_BUTTON, self.btnZero )
        self.m_button31.Bind( wx.EVT_BUTTON, self.OnDot )
        self.m_button32.Bind( wx.EVT_BUTTON, self.btnEqual )
        self.m_button40.Bind( wx.EVT_BUTTON, self.btnBracket1 )
        self.m_button41.Bind( wx.EVT_BUTTON, self.btnBracket2 )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def btnPer( self, event ):
        # self.txt_res.AppendText('/100')
        num = eval(self.txt_res.GetValue()+'/100.0') #+self.txt_res.GetValue())
        self.txt_res.SetValue(str(num))
        event.Skip()
    
    def btnClear( self, event ):
        # if self.txt_res:
        #     return
        # self.display.setText("0")
        # self.txt_res = ""
        # self.txt_res = True
        
        event.Skip()
    
    def btnAllClear( self, event ):
        self.txt_res.Clear()
        event.Skip()
    
    def btnDelete( self, event ):
        formula = self.txt_res.GetValue()
        self.txt_res.Clear()
        #맨오른쪽 값을 뺀 나머지 값을 셋팅함
        self.txt_res.SetValue(formula[:-1])
        event.Skip()
    
    def btnDivideX( self, event ):
        num = eval('1/'+self.txt_res.GetValue())
        self.txt_res.SetValue(str(num))
        event.Skip()
    
    def btnSqrX( self, event ):
        num = eval(self.txt_res.GetValue()+'*'+self.txt_res.GetValue())
        self.txt_res.SetValue(str(num))
        event.Skip()
    
    def btnRootX( self, event ):
        num = eval(self.txt_res.GetValue()+'**0.5')
        self.txt_res.SetValue(str(num))
        event.Skip()
    
    def btnDivide( self, event ):
        self.txt_res.AppendText('/')
        event.Skip()
    
    def btnSeven( self, event ):
        self.txt_res.AppendText('7')
        event.Skip()
    
    def btnEight( self, event ):
        self.txt_res.AppendText('8')
        event.Skip()
    
    def btnNine( self, event ):
        self.txt_res.AppendText('9')
        event.Skip()
    
    def btnMultiply( self, event ):
        self.txt_res.AppendText('*')
        event.Skip()
    
    def btnFour( self, event ):
        self.txt_res.AppendText('4')
        event.Skip()
    
    def btnFive( self, event ):
        self.txt_res.AppendText('5')
        event.Skip()
    
    def btnSIx( self, event ):
        self.txt_res.AppendText('6')
        event.Skip()
    
    def btnMinus( self, event ):
        self.txt_res.AppendText('-')
        event.Skip()
    
    def btnOne( self, event ):
        self.txt_res.AppendText('1')
        event.Skip()
    
    def btnTwo( self, event ):
        self.txt_res.AppendText('2')
        event.Skip()
    
    def btnThree( self, event ):
        self.txt_res.AppendText('3')
        event.Skip()
    
    def btnPlus( self, event ):
        self.txt_res.AppendText('+')
        event.Skip()
    
    def btnPosiNega( self, event ):
        try:
            res = -((int))(self.txt_res.GetValue())
            self.txt_res.SetValue(str(res))
        except:
            res = 'error!'
            self.txt_res.SetValue(res)
        event.Skip()
    
    def btnZero( self, event ):
        self.txt_res.AppendText('0')
        event.Skip()
    
    def OnDot( self, event ):
        self.txt_res.AppendText('.')
        event.Skip()
    
    def btnEqual( self, event ):
        try:
            res = eval(self.txt_res.GetLineText(0))
            self.txt_res.SetValue(str(res))
        except:
            res = 'error!'
            self.txt_res.SetValue(res)
        event.Skip()
    
    def btnBracket1( self, event ):
        self.txt_res.AppendText('(')
        event.Skip()
    
    def btnBracket2( self, event ):
        self.txt_res.AppendText(')')
        event.Skip()
    
    def Display( self, event ):
        if self.txt_res.GetLineText(0) == '0':
            self.txt_res.SetValue('')
        self.txt_res.AppendText(event.GetEventObject().GetLabel())
        event.Skip()
    
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame2(parent=None)
    frame.Show()
    app.MainLoop()

