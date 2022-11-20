from plotter import Plotter
import matplotlib.pyplot as plt
import read_write
import PIP
import Geometry

def main():
    plotter = Plotter()
    print('read polygon.csv')
    polygon_filepath = 'polygon.csv'
    polygon_idlist , polygon_xlist , polygon_ylist = read_write.readpolygon(polygon_filepath).read_polygon()
    #print(polygon_id , polygon_xlist , polygon_ylist)

    print('read input.csv')
    input_filepath = 'input.csv'
    xy_id , x_list , y_list = read_write.readinput(input_filepath).read_input()
    #print(xy_id , x_list , y_list)

    print('categorize points')
    polygon_points_list = read_write.getpointslist(polygon_idlist , polygon_xlist , polygon_ylist).get_points_list()
    input_points_list = read_write.getpointslist(xy_id , x_list , y_list).get_points_list()
    #print(polygon_points_list)
    #print(input_points_list)
    output_list = []
    for point in input_points_list:
        result = PIP.PIP(point , polygon_points_list).isPointinPolygon()
        output_list.append([point , result])
    #print(output_list)

    print('write output.csv')
    id = []
    category = []
    for i in output_list:
        id.append(i[0][0])
        category.append(i[1])
    write_filepath = 'output.csv'
    read_write.writeoutput(write_filepath , id , category).write_output()

    print('plot polygon and points')
    plotter.add_polygon(polygon_xlist , polygon_ylist)
    for output in output_list:
        plotter.add_point(output[0][1] , output[0][2] , output[1])
    plotter.show()

if __name__ == '__main__':
    main()
