# find in class RefineDialogNew(ui.ScriptWindow) this function

	def __LoadScript(self):

# this line

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.CancelRefine))

# add below

		if app.ENABLE_REFINE_RENEWAL:
			self.checkBox = ui.ToggleSwitch()
			self.checkBox.SetParent(self)
			self.checkBox.SetPosition(-55, 90)
			self.checkBox.SetWindowHorizontalAlignCenter()
			self.checkBox.SetWindowVerticalAlignBottom()
			self.checkBox.SetEvent(ui.__mem_func__(self.AutoRefine), "ON_CHECK", True)
			self.checkBox.SetEvent(ui.__mem_func__(self.AutoRefine), "ON_UNCHECK", False)
			self.checkBox.SetCheckStatus(constInfo.IS_AUTO_REFINE)
			self.checkBox.SetTextInfo(localeInfo.KEEP_REFINE_WINDOW_OPEN, -10, 0)
			self.checkBox.Show()

# find

	def Destroy(self):

# add below under the function

	if app.ENABLE_REFINE_RENEWAL:
		def __InitializeOpen(self):
			self.children = []
			self.vnum = 0
			self.targetItemPos = 0
			self.dialogHeight = 0
			self.cost = 0
			self.percentage = 0
			self.type = 0
			self.xRefineStart = 0
			self.yRefineStart = 0
# find

	def Open(self, targetItemPos, nextGradeItemVnum, cost, prob, type):

# edit this line

		self.__Initialize()

# to this line

		if app.ENABLE_REFINE_RENEWAL:
			self.__InitializeOpen()
		else:
			self.__Initialize()

# find

	def AppendMaterial(self, vnum, count):

# edit this line

		newHeight = self.dialogHeight + 75

# to this line

		if app.ENABLE_REFINE_RENEWAL:
			newHeight = self.dialogHeight + 105
		else:
			newHeight = self.dialogHeight + 75

# find

	def Accept(self):
		net.SendRefinePacket(self.targetItemPos, self.type)
		self.Close()

# add below

	if app.ENABLE_REFINE_RENEWAL:
		def AutoRefine(self, checkType, autoFlag):
			constInfo.IS_AUTO_REFINE = autoFlag
		
		def CheckRefine(self, isFail):
			if constInfo.IS_AUTO_REFINE == True:
				if constInfo.AUTO_REFINE_TYPE == 1:
					if constInfo.AUTO_REFINE_DATA["ITEM"][0] != -1 and constInfo.AUTO_REFINE_DATA["ITEM"][1] != -1:
						scrollIndex = player.GetItemIndex(constInfo.AUTO_REFINE_DATA["ITEM"][0])
						itemIndex = player.GetItemIndex(constInfo.AUTO_REFINE_DATA["ITEM"][1])
						
					#	chat.AppendChat(chat.CHAT_TYPE_INFO, "%d %d" % (itemIndex, int(itemIndex %10)))
						if scrollIndex == 0 or (itemIndex % 10 == 8 and not isFail):
							self.Close()
						else:
							net.SendItemUseToItemPacket(constInfo.AUTO_REFINE_DATA["ITEM"][0], constInfo.AUTO_REFINE_DATA["ITEM"][1])
				elif constInfo.AUTO_REFINE_TYPE == 2:
					npcData = constInfo.AUTO_REFINE_DATA["NPC"]
					if npcData[0] != 0 and npcData[1] != -1 and npcData[2] != -1 and npcData[3] != 0:
						itemIndex = player.GetItemIndex(npcData[1], npcData[2])
						if (itemIndex % 10 == 8 and not isFail) or isFail:
							self.Close()
						else:
							net.SendGiveItemPacket(npcData[0], npcData[1], npcData[2], npcData[3])
				else:
					self.Close()
			else:
				self.Close()