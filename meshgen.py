
# python packages
import numpy as np

# meshgen imports
from meshgen.inputfile import InputFile, InputSection
from meshgen.mesh import Mesh, Beam3rHerm2Lin3, Material, ContainerGeom, BC,\
    GeometrySet, Node, Function




# 
# 
# # create line
# cantilever = BeamMesh()
# cantilever.add_mesh_line(Beam3rHerm2Lin3, np.array([0,0,0]), np.array([10,0,0]), 10)
# end_beam = BeamMesh()
# end_beam.add_mesh_line(Beam3rHerm2Lin3, np.array([10,0,0]), np.array([15,0,0]), 5)
# end_beam.rotate(Rotation([0,0,1],np.pi/2), [10,0,0])
# 
# cantilever.add_mesh(end_beam)

# 
# 
# input2 = InputFile(maintainer='Ivo Steinbrecher', description='asd sakf ajsaf slkf jsalkfja sklfj salkfj saklfj salkff')
# # input2.geometry = cantilever
# #input2.get_dat_lines()
# 
# # print(input2._get_header())
# # 
# # print('end')
# # 
# # 
# # test = InputSection('sdf',['1','2'])
# # tmp = test.get_dat_lines()
# # print(tmp)
# 
# 
# sec = InputSection("STRUCTURAL DYNAMIC",
#                    """INT_STRATEGY                    Standard""")
# sec2 = InputSectionNodes()
# input2.add_section(sec)
# input2.add_section(sec)
# input2.add_section(sec2)
# 
# cantilever = BeamMesh()
# cantilever.add_mesh_line(Beam3rHerm2Lin3, np.array([0,0,0]), np.array([10,0,0]), 3)
# input2.geometry = cantilever
# 
# print(input2.sections)
# print(input2.get_string(header=False))
# 
# 
# 
# 
# a = BaciLine('test')
# print(str(a))
# 
# 
# 
# 
# print('end')


def line_test():
    """
    Test the BaciLine object
    """
    
    # only test
    tmp = InputLine('text')
    print(tmp)
    print()
    
    # only comment
    tmp = InputLine('// comment')
    print(tmp)
    print()
    
    # text with comment
    tmp = InputLine('var // comment')
    print(tmp)
    print()
    
    # var with value
    tmp = InputLine('var val    // comment')
    print(tmp)
    print()
    
    # no newline
    tmp = InputLine('var \n val comment')
    print(tmp)
    print()
    
    # get with var an val
    tmp = InputLine('var', 'val')
    print(tmp)
    print()
    
    # get with var an val with comment
    tmp = InputLine('var', 'val', option_comment='comment')
    print(tmp)
    print()
    
    # if there is an equal sign the string is split there
    tmp = InputLine('var = val')
    print(tmp)
    print()


def test_section():
    """
    Create some test sections
    """

    sec = InputSection("STRUCTURAL DYNAMIC", """INT_STRATEGY                    Standard
    test 2 //test
    test 4    """
    )
    for line in sec.get_dat_lines():
        print(line)
    print()

    sec = InputSection("STRUCTURAL DYNAMIC", """INT_STRATEGY                    Standard
    test 2 //test
    test 4    """, option_overwrite=True)
    sec.add_option('test', 100, option_overwrite=True)
    for line in sec.get_dat_lines():
        print(line)
    print()


def test_input():
    """
    Create a sample input file
    """

    # create input file
    input = InputFile(maintainer='Joe Doe', description='Simple input file')
    
    # add section with string
    input.add_section_by_data('PROBLEM SIZE', 'DIM 3')
    
    # add section with long string
    input.add_section_by_data(
        'IO/RUNTIME VTK OUTPUT/BEAMS',
        '''
        OUTPUT_BEAMS                    Yes
        DISPLACEMENT                    Yes
        USE_ABSOLUTE_POSITIONS          Yes
        TRIAD_VISUALIZATIONPOINT        Yes
        STRAINS_GAUSSPOINT              Yes
        INTERNAL_ENERGY_ELEMENT         Yes
        ''')
    
    # add section as object
    sec = InputSection('PROBLEM TYP')
    sec.add_option('PROBLEMTYP', 'Structure')
    sec.add_option('RESTART', '0')
    input.add_section(sec)
    
    # add section with equal arguments    
    input.add_section(InputSection(
        'STRUCT NOX/Printing',
        '''
        Outer Iteration                 = Yes
        Inner Iteration                 = No
        Outer Iteration StatusTest      = No
        Linear Solver Details           = No
        Test Details                    = No
        Debug                           = No
        '''
        ))
    
    # delete section
    input.delete_section('IO/RUNTIME VTK OUTPUT/BEAMS')
    input.delete_section('IO/RUNTIME VTK OUTPUT/BEAMS')
    
    # add to section
    input.add_section(InputSection(
        'STRUCT NOX/Printing',
        '''
        Outer Iteration StatusTest      = Yes // this value is overwriten
        Test                            = Maybe // this value is added
        ''', option_overwrite=True))
    input.add_section_by_data(
        'STRUCT NOX/Printing',
        '''
        Outer Iteration StatusTest      = No // this value is overwriten again
        Test                            = Sure // this value is added and overwritten
        ''', option_overwrite=True)

    # add node section
    input.add_section_by_data('NODE COORDS', [
        'NODE 394 COORD 2.00000000e+00 1.00000000e+00 -2.00000003e-01',
        'NODE 395 COORD 2.00000000e+00 1.00000000e+00 -6.00000024e-01',
        'NODE 396 COORD 2.00000000e+00 1.00000000e+00 -1.00000000e+00'])
    
    # add element section
    input.add_section_by_data('STRUCTURE ELEMENTS', [
'1 BEAM3R HERM2LIN3 1 3 2 MAT 1 TRIADS 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 FAD',
'2 BEAM3R HERM2LIN3 3 5 4 MAT 1 TRIADS 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 FAD',
'3 BEAM3R HERM2LIN3 5 7 6 MAT 1 TRIADS 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 FAD',
'4 BEAM3R HERM2LIN3 7 9 8 MAT 1 TRIADS 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 FAD',
'5 BEAM3R HERM2LIN3 9 11 10 MAT 1 TRIADS 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 FAD',
'6 BEAM3R HERM2LIN3 11 13 12 MAT 1 TRIADS 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 FAD'])
    
    # add coupling section
    input.add_section_by_data('DESIGN POINT COUPLING CONDITIONS', [
'DPOINT 100',
'E 5 - NUMDOF 9 ONOFF 1 1 1 1 1 1 0 0 0',
'E 6 - NUMDOF 9 ONOFF 1 1 1 1 1 1 0 0 0',
'E 7 - NUMDOF 9 ONOFF 1 1 1 1 1 1 0 0 0',
'E 8 - NUMDOF 9 ONOFF 1 1 1 1 1 1 0 0 0'
])

    # add mesh
    cantilever = Mesh()
    nodes1, tmp, tmp, tmp = cantilever.add_beam_mesh_line(Beam3rHerm2Lin3, np.array([0, 0, 0]), np.array([10, 2, 5]), 3000)
    nodes2, tmp, tmp, tmp = cantilever.add_beam_mesh_line(Beam3rHerm2Lin3, np.array([0, 0, 0]), np.array([9, 1, 4]), 3000)
    cantilever.add_coupling([nodes1[0], nodes2[0]], 'NUMDOF 9 ONOFF 1 1 1 1 1 1 0 0 0')
    input.mesh = cantilever
    
    print(input.get_string())


def test_sets():
    cantilever = Mesh()
    cantilever.add_beam_mesh_line(Beam3rHerm2Lin3, np.array([0, 0, 0]), np.array([10, 2, 5]), 3000, add_sets=False)
    print(cantilever)
    print(cantilever.point_sets)
    print(cantilever.line_sets)





































def beam_and_solid():
    
    # create input file
    input_file = InputFile(maintainer='Joe Doe', description='Simple input file')
    
    # load solid mesh
    input_file.read_dat('input/block.dat')
    
    # delete solver 2 section
    input_file.delete_section('TITLE')
    
    # add options for beam_output
    input_file.add_section(InputSection(
        'IO/RUNTIME VTK OUTPUT/BEAMS',
        '''
        OUTPUT_BEAMS                    Yes
        DISPLACEMENT                    Yes
        USE_ABSOLUTE_POSITIONS          Yes
        TRIAD_VISUALIZATIONPOINT        Yes
        STRAINS_GAUSSPOINT              Yes
        '''))
    
    # add a straight line beam
    material = Material('MAT_BeamReissnerElastHyper', 1e9, 0, 1e-3, 0.5)
    cantilever = Mesh(name='cantilever')
    cantilever_set = cantilever.add_beam_mesh_line(Beam3rHerm2Lin3, material, [2,0,-5], [2,0,5], 3)
    
    # add fix at start of the beam
    cantilever.add_bc(
        'dirich',
        BC(
            cantilever_set.point[0], # bc set
            'NUMDOF 9 ONOFF 1 1 1 1 1 1 0 0 0 VAL 0 0 0 0 0 0 0 0 0 FUNCT 0 0 0 0 0 0 0 0 0' # bc string
            )
        )
    
    # add displacement controlled bc at end of the beam
    sin = Function('COMPONENT 0 FUNCTION sin(t*2*pi)')
    cos = Function('COMPONENT 0 FUNCTION 1-cos(t*2*pi)')
    cantilever.add_function(sin)
    cantilever.add_function(cos)
    cantilever.add_bc(
        'dirich',
        BC(
            cantilever_set.point[1], # bc set
            'NUMDOF 9 ONOFF 1 1 1 1 1 1 0 0 0 VAL 1 1 0 0 0 0 0 0 0 FUNCT {} {} 0 0 0 0 0 0 0', # bc string
            format_replacement=[cos,sin]
            )
        )
    
    # add the beam mesh to the solid mesh
    input_file.add_mesh(cantilever)
       
    
#     # print input file
#     for line in input_file.get_dat_lines(header=True, print_all_sets=False, print_set_names=True):
#         print(line)
#     

    # write input file
    input_file.write_input_file('/home/ivo/dev/inputgenerator-py/input/meshgen.dat')




#     set_line2 = cantilever.add_beam_mesh_line(Beam3rHerm2Lin3, material, [5,6,10], [1,2,3], 5)
#     cantilever.add_bc('dirich', BC(set_line2[__POINT__][0], 'NUMDOF 6 ONOFF 1 1 1 0 0 0 VAL 0.0 0.0 0.0 0.0 0.0 0.0 FUNCT 0 {} {} 0 0 0', format_replacement=[f2, '6666',22]))
#     bc = BC(set_line2[__LINE__][0], 'asdfasdf')
#     cantilever.add_bc('dirich', bc)
# #     cantilever.add_bc('dirich', BC(set_line2[__POINT__][1], 'asdfasdf'))
# #     sets = GeometrySet('start', [Node([0,0,0])])
# #     cantilever.add_bc('dirich', BC('asdfasdf', sets))

    
    #cantilever.add_function(f2)

    








# line_test()
# test_section()
# test_input()
# test_sets()
beam_and_solid()
