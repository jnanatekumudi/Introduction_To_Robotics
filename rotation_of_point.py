import math


def get_point():
    print("Enter the coordinates of the point in the frame to be shifted as x y z: ", end=" ")
    coords = [0, 0, 0]
    while(1):
        coords = list(map(int, input().strip().split()))
        if len(coords) > 3:
            print(f"Expected 3 values, more than 3 values entered. Did you mean: {coords[0], coords[1], coords[2]}? (y/n) ", end="")
            reply = input()
            if reply == "y":
                coords = coords[:3]
                return coords
            elif reply == "n":
                print("Enter the coordinates the point again: ", end="")
            else:
                print("Invalid input")
                break
        else:
            break
    return coords[:3]


def get_rotation():
    print("Enter the angles of rotation of the frame to be shifted about the x y z coordinates in degrees: ", end="")
    angles = [0, 0, 0]
    while(1):
        angles = list(map(int, input().strip().split()))
        if len(angles) > 3:
            print(f"Expected 3 values, more than 3 values entered. Did you mean: {angles[0], angles[1], angles[2]}? (y/n) ", end="")
            reply = input()
            if reply == "y":
                angles = angles[:3]
                return angles
            elif reply == "n":
                print("Enter the angles of rotation again: ", end="")
            else:
                print("Invalid input")
                break
        else:
            break
    return angles[:3]


def compute_transform(on_X, on_Y):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(on_X)):
        for j in range(len(on_Y[0])):
            for k in range(len(on_Y)):
                result[i][j] += (on_X[i][k] * on_Y[k][j])
    return result


def transform_point(apply_transform, on_point):
    result = [0, 0, 0]
    for i in range(len(apply_transform)):
        for j in range(len(on_point)):
            result[i] += (apply_transform[i][j] * on_point[j])
    return result


def get_transform(coords, angles):
    
    x_rotation_matrix = [
        [1, 0, 0],
        [0, math.cos(math.radians(angles[0])), - math.sin(math.radians(angles[0]))],
        [0, math.sin(math.radians(angles[0])), math.cos(math.radians(angles[0]))],
    ]

    y_rotation_matrix = [
        [math.cos(math.radians(angles[1])), 0, math.sin(math.radians(angles[1]))],
        [0, 1, 0],
        [-math.sin(math.radians(angles[1])), 0, math.cos(math.radians(angles[1]))],
    ]

    z_rotation_matrix = [
        [math.cos(math.radians(angles[2])), - math.sin(math.radians(angles[2])), 0],
        [math.sin(math.radians(angles[2])), math.cos(math.radians(angles[2])), 0],
        [0, 0, 1],
    ]

    transformation = compute_transform(x_rotation_matrix, y_rotation_matrix)
    transformation = compute_transform(transformation, z_rotation_matrix)
    point_in_FrameA = transform_point(transformation, coords)

    print(f"\nCoordinates of the point {coords[0], coords[1], coords[2]} with respect to original frame is {round(point_in_FrameA[0], 3), round(point_in_FrameA[1], 3), round(point_in_FrameA[2], 3)}")


if __name__ == "__main__":
    coords = get_point()
    angles = get_rotation()

    get_transform(coords, angles)
    print("\nComputation finished.")
