import typing
import xml.etree.ElementTree as ET

from OMSimulator import Scope, System, Types


class Model:
  def __init__(self, cref: str):
    if cref not in Scope._Scope:
      raise Exception("Model doesn't exists")
    self._cref = cref

  def delete(self):
    Scope.clearLoggingBuffer()
    status = Scope._capi.delete(self.cref)
    if Types.Status(status) == Types.Status.OK:
      Scope._Scope = [cref for cref in Scope._Scope if cref != self.cref]
    else:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def addSystem(self, cref: str, type_: Types.System):
    Scope.clearLoggingBuffer()
    new_cref = self.cref + '.' + cref
    status = Scope._capi.addSystem(new_cref, type_.value)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return System.System(new_cref)

  def exportDependencyGraphs(self, initialization: str, event: str, simulation: str) -> None:
    Scope.clearLoggingBuffer()
    status = Scope._capi.exportDependencyGraphs(self.cref, initialization, event, simulation)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def instantiate(self):
    Scope.clearLoggingBuffer()
    status = Scope._capi.instantiate(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def initialize(self):
    Scope.clearLoggingBuffer()
    status = Scope._capi.initialize(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def simulate(self):
    Scope.clearLoggingBuffer()
    status = Scope._capi.simulate(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def doStep(self):
    Scope.clearLoggingBuffer()
    status = Scope._capi.doStep(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def stepUntil(self, stopTime: float):
    Scope.clearLoggingBuffer()
    status = Scope._capi.stepUntil(self.cref, stopTime)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def terminate(self):
    Scope.clearLoggingBuffer()
    status = Scope._capi.terminate(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def reset(self):
    Scope.clearLoggingBuffer()
    status = Scope._capi.reset(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def getAllSignals(self):
    allSignals = {}
    signalFilter = self.exportSnapshot(':resources/signalFilter.xml')
    root = ET.fromstring(signalFilter)
    for var in root[0][0]:
      name = var.attrib['name']
      type_ = var.attrib['type']
      kind = var.attrib['kind']
      allSignals[name] = {'type': type_, 'kind': kind}
    return allSignals

  def getBoolean(self, cref: str):
    Scope.clearLoggingBuffer()
    value, status = Scope._capi.getBoolean(self.cref + '.' + cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return value

  def getInteger(self, cref: str):
    Scope.clearLoggingBuffer()
    value, status = Scope._capi.getInteger(self.cref + '.' + cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return value

  def getReal(self, cref: str):
    Scope.clearLoggingBuffer()
    value, status = Scope._capi.getReal(self.cref + '.' + cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return value

  def getString(self, cref: str):
    Scope.clearLoggingBuffer()
    value, status = Scope._capi.getString(self.cref + '.' + cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return value

  def setBoolean(self, cref: str, value: bool) -> None:
    Scope.clearLoggingBuffer()
    status = Scope._capi.setBoolean(self.cref + '.' + cref, value)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def setInteger(self, cref: str, value: int) -> None:
    Scope.clearLoggingBuffer()
    status = Scope._capi.setInteger(self.cref + '.' + cref, value)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def setReal(self, cref: str, value: float) -> None:
    Scope.clearLoggingBuffer()
    status = Scope._capi.setReal(self.cref + '.' + cref, value)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def setString(self, cref: str, value: str) -> None:
    Scope.clearLoggingBuffer()
    status = Scope._capi.setString(self.cref + '.' + cref, value)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def exportSnapshot(self, ident: str = None) -> str:
    Scope.clearLoggingBuffer()
    contents, status = Scope._capi.exportSnapshot(self.cref + ('.' + ident if ident else ''))
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return contents

  def exportSSVTemplate(self, ident: str, filename: str) -> None:
    Scope.clearLoggingBuffer()
    status = Scope._capi.exportSSVTemplate(self.cref + ('.' + ident if ident else ''), filename)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  def setLoggingInterval(self, loggingInterval: float) -> None:
    Scope.clearLoggingBuffer()
    status = Scope._capi.setLoggingInterval(self.cref, loggingInterval)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  @property
  def cref(self):
    return self._cref

  @property
  def time(self):
    Scope.clearLoggingBuffer()
    value, status = Scope._capi.getTime(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return value

  @property
  def startTime(self):
    Scope.clearLoggingBuffer()
    value, status = Scope._capi.getStartTime(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return value

  @startTime.setter
  def startTime(self, value: float):
    Scope.clearLoggingBuffer()
    status = Scope._capi.setStartTime(self.cref, value)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  @property
  def stopTime(self):
    Scope.clearLoggingBuffer()
    value, status = Scope._capi.getStopTime(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return value

  @stopTime.setter
  def stopTime(self, value: float):
    Scope.clearLoggingBuffer()
    status = Scope._capi.setStopTime(self.cref, value)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  @property
  def resultFile(self):
    Scope.clearLoggingBuffer()
    file, _, status = Scope._capi.getResultFile(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return file

  @resultFile.setter
  def resultFile(self, file: str):
    Scope.clearLoggingBuffer()
    _, bufferSize, status = Scope._capi.getResultFile(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

    status = Scope._capi.setResultFile(self.cref, file, bufferSize)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  @property
  def fixedStepSize(self):
    Scope.clearLoggingBuffer()
    stepSize, status = Scope._capi.getFixedStepSize(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return stepSize

  @fixedStepSize.setter
  def fixedStepSize(self, stepSize: float):
    Scope.clearLoggingBuffer()
    status = Scope._capi.setFixedStepSize(self.cref, stepSize)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')

  @property
  def modelState(self):
    Scope.clearLoggingBuffer()
    modelState, status = Scope._capi.getModelState(self.cref)
    if Types.Status(status) != Types.Status.OK:
      raise Exception(f'status={Types.Status(status).name} {Scope._Logging}')
    return Types.ModelState(modelState)
