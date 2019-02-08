-- status: correct
-- teardown_command: rm -rf Example_res.mat Example.log
-- linux: yes
-- mingw: no
-- win: no

oms_setCommandLineOption("--suppressPath=true --ignoreInitialUnknowns=true --stripRoot=true")
oms_setTempDirectory("./ASSCExample-lua/")

oms_newModel("Example")
oms_addSystem("Example.root", oms_system_sc)

-- instantiate FMUs
oms_addSubModel("Example.root.Class1", "../resources/ASSCExample.Class1.fmu")
oms_addSubModel("Example.root.Class2", "../resources/ASSCExample.Class2.fmu")

-- add connections
oms_addConnection("Example.root.Class1.max", "DualMassOscillator.root.Class2.max")


oms_setStopTime("Example", 6.0)
oms_setSolver("Example", oms_solver_wc_assc)
oms_setVariableStepSize("Example", 0.05, 0.05, 0.5)

oms_addEventIndicator("Example.Class1.max")
oms_addTimeIndicator("Example.Class1.eventTime")
oms_addStaticValueIndicator("Example.Class2.signalwiththreshold", 4.5, 5.0, 0.1)
oms_addDynamicValueIndicator("Example.Class2.signalwiththreshold", "Example.Class1.closeToMax", "Example.Class1.max", 0.05)

oms_instantiate("Example")
oms_initialize("Example")
oms_simulate("Example")
oms_terminate("Example")
oms_delete("Example")

if 1 == oms_compareSimulationResults("Example_res.mat", "../references/SSC.mat", "Class2.signalwiththreshold", 0.0, 0.0) then
  print("info:     Results are equal")
else
  print("warning:  Results are not equal")
end

-- Result:
-- stdout            | info    | The initialization finished successfully without homotopy method.
-- stdout            | info    | The initialization finished successfully without homotopy method.
-- info:    Results are equal
-- info:    Logging information has been saved to "Example.log"
-- endResult
