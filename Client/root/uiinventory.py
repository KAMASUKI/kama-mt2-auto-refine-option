# find

	def RefineItem(self, scrollSlotPos, targetSlotPos):

		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if player.REFINE_OK != player.CanRefine(scrollIndex, targetSlotPos):
			return

		self.__SendUseItemToItemPacket(scrollSlotPos, targetSlotPos)
		return

# under this line

		if player.REFINE_OK != player.CanRefine(scrollIndex, targetSlotPos):
			return

# add this

		if app.ENABLE_REFINE_RENEWAL:
			constInfo.AUTO_REFINE_TYPE = 1
			constInfo.AUTO_REFINE_DATA["ITEM"][0] = scrollSlotPos
			constInfo.AUTO_REFINE_DATA["ITEM"][1] = targetSlotPos

# like this

	def RefineItem(self, scrollSlotPos, targetSlotPos):

		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if player.REFINE_OK != player.CanRefine(scrollIndex, targetSlotPos):
			return

		if app.ENABLE_REFINE_RENEWAL:
			constInfo.AUTO_REFINE_TYPE = 1
			constInfo.AUTO_REFINE_DATA["ITEM"][0] = scrollSlotPos
			constInfo.AUTO_REFINE_DATA["ITEM"][1] = targetSlotPos

		self.__SendUseItemToItemPacket(scrollSlotPos, targetSlotPos)
		return