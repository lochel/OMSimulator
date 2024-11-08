-- status: correct
-- teardown_command: rm -rf EventTest_lua/
-- linux: no
-- ucrt64: yes
-- win: yes
-- mac: no

oms_setCommandLineOption("--suppressPath=true")
oms_setTempDirectory("./EventTest_lua/")
oms_setWorkingDirectory("./EventTest_lua/")

oms_newModel("EventTest")
oms_addSystem("EventTest.root", oms_system_sc)
oms_addSubModel("EventTest.root.model", "../../resources/EventTest.fmu")

-- simulation settings
oms_setResultFile("model", "EventTest_lua.csv")
oms_setStopTime("model", 10.0
oms_setFixedStepSize("model.root", 1.0)

oms_instantiate("EventTest")
oms_setReal("EventTest.root.model.start_height", 0.3)
oms_initialize("EventTest")
oms_simulate("EventTest")
oms_terminate("EventTest")
oms_delete("EventTest")

-- Result:
-- endResult
