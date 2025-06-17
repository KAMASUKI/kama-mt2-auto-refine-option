# find

def GetHyperlink():
	return wndMgr.GetHyperlink()

# add below

if app.ENABLE_REFINE_RENEWAL:
	import math
	MAIN_PATH = "d:/ymir work/ui/game/toggle_switch/"
	class ToggleSwitch(Window):
		def __init__(self):
			Window.__init__(self)
			self._Initialize()
			self.CreateElements()
			
		def __del__(self):
			Window.__del__(self)
			self._Initialize()
		
		def _Initialize(self):
			self.backgroundImage = None
			self.checkImage = None
			
			self.eventFunc = { "ON_CHECK" : None, "ON_UNCHECK" : None, }
			self.eventArgs = { "ON_CHECK" : None, "ON_UNCHECK" : None, }
			
			self.isChecked = False
			self.animationProgress = 0
			self.animationDuration = 10
			self.isAnimating = False
			
			self.uncheckedXPosition = 0
			self.checkedXPosition = 13
			self.animationDistance = self.checkedXPosition - self.uncheckedXPosition
		
		def CreateElements(self):
			self.backgroundImage = ImageBox()
			self.backgroundImage.SetParent(self)
			self.backgroundImage.AddFlag("not_pick")
			self.backgroundImage.SetPosition(0, 0)
			self.backgroundImage.LoadImage(MAIN_PATH + "bg.tga")
			self.backgroundImage.Show()
			
			self.checkImage = ImageBox()
			self.checkImage.SetParent(self.backgroundImage)
			self.checkImage.AddFlag("not_pick")
			self.checkImage.SetPosition(self.uncheckedXPosition, 0)
			self.checkImage.LoadImage(MAIN_PATH + "unchecked.tga")
			self.checkImage.Show()
			
			self.textInfo = TextLine()
			self.textInfo.SetParent(self)
			self.textInfo.SetPosition(0, 0)
			self.textInfo.SetWindowHorizontalAlignRight()
			self.textInfo.Show()
			
			self.SetSize(self.backgroundImage.GetWidth(), self.backgroundImage.GetHeight())
			
			self.backgroundImage.SetWindowHorizontalAlignCenter()
			
		def SetTextInfo(self, info, x = 50, y = 0):
			if self.textInfo:
				self.textInfo.SetText(info)
				self.textInfo.SetPosition(x, y)
			
		def SetCheckStatus(self, flag):
			if flag != self.isChecked:
				self.isChecked = flag
				self.StartAnimation()
		
		def GetCheckStatus(self):
			if self.checkImage:
				return self.isChecked
				
			return False
			
		def SetEvent(self, func, *args) :
			result = self.eventFunc.has_key(args[0])		
			if result :
				self.eventFunc[args[0]] = func
				self.eventArgs[args[0]] = args
			else :
				print "[ERROR] ui.py SetEvent, Can`t Find has_key : %s" % args[0]
			
		def OnMouseLeftButtonUp(self):
			if not self.isAnimating:
				self.isChecked = not self.isChecked
				self.StartAnimation()
	
				if self.isChecked and self.eventFunc["ON_CHECK"]:
					apply(self.eventFunc["ON_CHECK"], self.eventArgs["ON_CHECK"])
				elif not self.isChecked and self.eventFunc["ON_UNCHECK"]:
					apply(self.eventFunc["ON_UNCHECK"], self.eventArgs["ON_UNCHECK"])
	
		def StartAnimation(self):
			self.isAnimating = True
			self.animationProgress = 0
			self.checkImage.Show()
	
		def OnRender(self):
			if self.isAnimating:
				self.animationProgress += 1
				progress = float(self.animationProgress) / self.animationDuration
	
				if progress <= 1:
					x_offset = int(math.sin(progress * math.pi / 2) * self.animationDistance)
					
					if self.isChecked:
						self.checkImage.SetPosition(self.uncheckedXPosition + x_offset, 0)
						self.checkImage.LoadImage(MAIN_PATH + "checked.tga")
					else:
						self.checkImage.SetPosition(self.checkedXPosition - x_offset, 0)
						self.checkImage.LoadImage(MAIN_PATH + "unchecked.tga")
				else:
					self.isAnimating = False
					self.animationProgress = 0
					
					if self.isChecked:
						self.checkImage.SetPosition(self.checkedXPosition, 0)
						self.checkImage.LoadImage(MAIN_PATH + "checked.tga")
					else:
						self.checkImage.SetPosition(self.uncheckedXPosition, 0)
						self.checkImage.LoadImage(MAIN_PATH + "unchecked.tga")