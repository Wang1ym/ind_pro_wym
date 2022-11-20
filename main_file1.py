from plotter import Plotter
import matplotlib.pyplot as plt
from pip_function import Geometry
from pip_function import Point
from pip_function import Line
from pip_function import Polygon
from pip_function import Readfile
from pip_function import PIP
from pip_function import Listtopointobject

def main(poly_path, ip_path):
    plotter = Plotter()
    print('read polygon.csv')
    # read polygon_file
    # polygon_filepath = 'polygon.csv'
    polygon_filepath = poly_path
    polygon_idlist, polygon_xlist, polygon_ylist = Readfile(polygon_filepath).read_file_list()
    # create a polygon object
    polygon_points = Listtopointobject(polygon_idlist, polygon_xlist, polygon_ylist).list_to_point_object()
    polygon = Polygon('POLYGON', polygon_points)


    print('read input.csv')
    # read input_file
    # input_filepath = 'input.csv'
    input_filepath = ip_path
    input_idlist, input_xlist, input_ylist = Readfile(input_filepath).read_file_list()
    # create a list of points odjects
    input_points = Listtopointobject(input_idlist, input_xlist, input_ylist).list_to_point_object()

    print('categorize points')
    output_list = []
    for point in input_points:
        result = PIP(point, polygon_points).isPointinPolygon()
        output_list.append([point.get_name(), point.get_x(), point.get_y(), result])
    print(output_list)

    print('plot polygon and points')
    plotter.add_polygon(polygon_xlist , polygon_ylist)
    for output in output_list:
        plotter.add_point(output[1] , output[2] , output[3])
    plotter.show()

if __name__ == '__main__':
    main('polygon.csv', 'input.csv')