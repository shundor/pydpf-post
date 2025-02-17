import pytest

from ansys.dpf import post
from ansys.dpf.post.result_definition import Definition


def test_resultdefinition_init(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    definition = stress.definition
    assert isinstance(definition, Definition)
    assert definition.location == post.locations.nodal
    stress2 = solution.stress(
        node_scoping=2, time_scoping=1, grouping=post.grouping.by_material
    )
    print(stress2)
    definition2 = stress2.definition
    assert definition2.node_scoping == 2
    assert definition2.time_scoping == 1
    assert definition2.grouping == post.grouping.by_material
    assert definition2.location == post.locations.nodal
    stress3 = solution.stress(
        element_scoping=2, time=0.1, location=post.locations.elemental
    )
    print(stress3)
    definition3 = stress3.definition
    assert definition3.element_scoping == 2
    assert definition3.time == 0.1
    assert definition3.location == post.locations.elemental
    stress4 = solution.stress(named_selection="SELECTION", set=1)
    print(stress4)
    definition4 = stress4.definition
    assert definition4.named_selection == "SELECTION"
    assert definition4.set == 1
    assert definition4.location == post.locations.nodal


def test_resdef_location(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.location == post.locations.nodal
    stress.definition.location = post.locations.elemental
    assert stress.definition.location == post.locations.elemental


def test_resdef_nodescoping(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.node_scoping == None
    stress.definition.node_scoping = 2
    assert stress.definition.node_scoping == 2


def test_resdef_elemscoping(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.element_scoping == None
    stress.definition.element_scoping = 2
    assert stress.definition.element_scoping == 2


def test_resdef_timescoping(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.time_scoping == None
    stress.definition.time_scoping = 2
    assert stress.definition.time_scoping == 2


def test_resdef_namedsel(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.named_selection == None
    stress.definition.named_selection = "S"
    assert stress.definition.named_selection == "S"


def test_resdef_grouping(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.grouping == None
    stress.definition.grouping = post.grouping.by_el_shape
    assert stress.definition.grouping == post.grouping.by_el_shape


def test_resdef_mapdlgrouping(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.mapdl_grouping == None
    stress.definition.mapdl_grouping = 186
    assert stress.definition.mapdl_grouping == 186


def test_resdef_time(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.time == None
    stress.definition.time = 0.1
    assert stress.definition.time == 0.1


def test_resdef_set(allkindofcomplexity):
    solution = post.load_solution(allkindofcomplexity)
    stress = solution.stress()
    assert stress.definition.set == None
    stress.definition.set = 3
    assert stress.definition.set == 3


@pytest.mark.skipif(
    True,
    reason=(
        "The location setting of electric_field result that was "
        "locked for versions lower than 0.2.0 is not locked anymore."
    ),
)
def test_location_locked_electric_field(rth_electric):
    solution = post.load_solution(rth_electric)
    ef = solution.electric_field(location="Nodal")
    with pytest.raises(Exception):
        ef.definition.location = None
    try:
        ef.definition.location = None
    except Exception as e:
        message = (
            "Location cannot be set outside of the instantiation "
            "of the result object in this case."
        )
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)


def test_elemscoping_locked_electric_field(rth_electric):
    solution = post.load_solution(rth_electric)
    with pytest.raises(Exception):
        solution.electric_field(element_scoping=[2])
    try:
        ef = solution.electric_field(element_scoping=[2])
    except Exception as e:
        message = "Element scoping is not available with thermal/electric results."
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)

    ef = solution.electric_field()
    with pytest.raises(Exception):
        ef.definition.element_scoping = [2]
    try:
        ef.definition.element_scoping = [2]
    except Exception as e:
        message = (
            "Element scoping cannot be set outside of the "
            "instantiation of the result object in this case."
        )
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)


def test_elemscoping_locked_electric_potential(rth_electric):
    solution = post.load_solution(rth_electric)
    with pytest.raises(Exception):
        solution.electric_potential(element_scoping=[2])
    try:
        ef = solution.electric_potential(element_scoping=[2])
    except Exception as e:
        message = "Element scoping is not available with thermal/electric results."
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)

    ef = solution.electric_potential()
    with pytest.raises(Exception):
        ef.definition.element_scoping = [2]
    try:
        ef.definition.element_scoping = [2]
    except Exception as e:
        message = (
            "Element scoping cannot be set outside of the "
            "instantiation of the result object in this case."
        )
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)


def test_elemscoping_locked_temperature(rth_electric):
    solution = post.load_solution(rth_electric)
    with pytest.raises(Exception):
        solution.temperature(element_scoping=[2])
    try:
        ef = solution.temperature(element_scoping=[2])
    except Exception as e:
        message = "Element scoping is not available with thermal/electric results."
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)

    ef = solution.temperature()
    with pytest.raises(Exception):
        ef.definition.element_scoping = [2]
    try:
        ef.definition.element_scoping = [2]
    except Exception as e:
        message = (
            "Element scoping cannot be set outside of the "
            "instantiation of the result object in this case."
        )
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)


def test_elemscoping_locked_heat_flux(rth_electric):
    solution = post.load_solution(rth_electric)
    with pytest.raises(Exception):
        solution.heat_flux(element_scoping=[2])
    try:
        ef = solution.heat_flux(element_scoping=[2])
    except Exception as e:
        message = "Element scoping is not available with thermal/electric results."
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)

    ef = solution.heat_flux()
    with pytest.raises(Exception):
        ef.definition.element_scoping = [2]
    try:
        ef.definition.element_scoping = [2]
    except Exception as e:
        message = (
            "Element scoping cannot be set outside of the "
            "instantiation of the result object in this case."
        )
        e2 = Exception(message)
        assert e.args == e2.args
        assert type(e) == type(e2)
