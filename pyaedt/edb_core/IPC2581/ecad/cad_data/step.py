from pyaedt.edb_core.IPC2581.ecad.cad_data.profile import Profile
from pyaedt.edb_core.IPC2581.ecad.cad_data.padstack_def.padstack_def import PadstackDef
from pyaedt.edb_core.IPC2581.ecad.cad_data.package.package import Package
from pyaedt.edb_core.IPC2581.ecad.cad_data.component.component import Component
from pyaedt.edb_core.IPC2581.ecad.cad_data.logical_net.logical_net import LogicalNets
from pyaedt.edb_core.IPC2581.ecad.cad_data.phy_net.phy_net import PhyNet
from pyaedt.edb_core.IPC2581.ecad.cad_data.layer_feature.layer_feature import LayerFeature


class Step(object):
    def __init__(self):
        self._name = ""
        self._datum = (0.0, 0.0)
        self._padstack_defs = []
        self._profile = Profile()
        self._packages = []
        self._components = []
        self._logical_nets = LogicalNets()
        self._physical_nets = []
        self._layer_features = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value

    @property
    def datum(self):
        return self._datum

    @datum.setter
    def datum(self, value):
        if isinstance(value, tuple):
            self._datum = value

    @property
    def padstack_defs(self):
        return self._padstack_defs

    @padstack_defs.setter
    def padstack_defs(self, value):
        if isinstance(value, list):
            if len([pad for pad in value if isinstance(pad, PadstackDef)]) == len(value):
                self._padstack_defs = value

    @property
    def packages(self):
        return self._packages

    @packages.setter
    def packages(self, value):
        if isinstance(value, list):
            if len([pkg for pkg in value if isinstance(pkg, Package)]) == len(value):
                self._packages = value

    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        if isinstance(value, list):
            if len([cmp for cmp in value if isinstance(cmp, Component)]) == len(value):
                self._components = value

    @property
    def logical_nets(self):
        return self._logical_nets

    @logical_nets.setter
    def logical_nets(self, value):
        if isinstance(value, LogicalNets):
            self._logical_nets = value

    @property
    def layer_features(self):
        return self._layer_features

    @layer_features.setter
    def layer_features(self, value):
        if isinstance(value, list):
            if len([feat for feat in value if isinstance(feat, )]):
                self._layer_features = value

    @property
    def physical_nets(self):
        return self._physical_nets

    @physical_nets.setter
    def physical_nets(self, value):
        if isinstance(value, list):
            if len([phy_net for phy_net in value if isinstance(phy_net, PhyNet)]) == len(value):
                self._physical_nets = value

    def add_physical_net(self, phy_net=None):
        if isinstance(phy_net, PhyNet):
            self._physical_nets.append(phy_net)
            return True
        return False

    def add_padstack_def(self, padstack_def=None):
        if isinstance(padstack_def, PadstackDef):
            self._padstack_defs.append(padstack_def)
            return True
        return False

    def add_package(self, package=None):
        if isinstance(package, Package):
            self._packages.append(package)
            return True
        return False

    def add_component(self, component=None):
        if isinstance(component, Component):
            self._components.append(component)
            return True
        return False

    def add_layer_feature(self, layer_feature=None):
        if isinstance(layer_feature, LayerFeature):
            self._layer_features.append(layer_feature)
            return True
        return False

    def write_xml(self):
        pass