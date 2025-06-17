// add to the file

#ifdef ENABLE_REFINE_RENEWAL
	PyModule_AddIntConstant(poModule, "ENABLE_REFINE_RENEWAL", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_REFINE_RENEWAL", 0);
#endif