{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Operator View',
          'size':(1168, 741),

         'components': [

{'type':'StaticText', 
    'name':'VmsResultWindow', 
    'position':(575, 15), 
    'font':{'faceName': 'Verdana', 'family': 'sansSerif', 'size': 12}, 
    'text':'Result Window', 
    },

{'type':'StaticText', 
    'name':'OperatorUI', 
    'position':(16, 159), 
    'font':{'style': 'bold', 'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'text':'Click On Image to Load Program.', 
    },

{'type':'StaticText', 
    'name':'Measure_Line', 
    'position':(32, 466), 
    'font':{'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':'"MeasureLine.voy"', 
    },

{'type':'StaticText', 
    'name':'MeasureCirle', 
    'position':(32, 336), 
    'font':{'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':'"MeasureCirle.voy"', 
    },

{'type':'ImageButton', 
    'name':'ImgBtnMeasureLine', 
    'position':(70, 379), 
    'size':(70, 72), 
    'border':'3d', 
    'file':'measure_square.gif', 
    'foregroundColor':(255, 255, 255, 255), 
    },

{'type':'ImageButton', 
    'name':'ImgBtnMeasureCircle', 
    'position':(64, 238), 
    'size':(83, 81), 
    'border':'3d', 
    'file':'measure_circle.gif', 
    'foregroundColor':(255, 255, 255, 255), 
    },

{'type':'TextArea', 
    'name':'ResultWindow', 
    'position':(234, 50), 
    'size':(882, 596), 
    'editable':False, 
    'horizontalScrollbar':True, 
    },

{'type':'Button', 
    'name':'BtnRunProgram', 
    'position':(66, 547), 
    'size':(87, -1), 
    'backgroundColor':(255, 128, 64, 255), 
    'label':'Run Program', 
    },

{'type':'Button', 
    'name':'BtnZero', 
    'position':(267, 12), 
    'size':(86, -1), 
    'backgroundColor':(192, 192, 192, 255), 
    'label':'&Zero Stage', 
    },

{'type':'Button', 
    'name':'BtnStopVMS', 
    'position':(999, 13), 
    'backgroundColor':(255, 0, 0, 255), 
    'label':'S&top VMS', 
    },

{'type':'Button', 
    'name':'BtnStartVMS', 
    'position':(64, 59), 
    'backgroundColor':(0, 255, 0, 255), 
    'label':'&Start VMS', 
    },

] # end components
} # end background
] # end backgrounds
} }
