import marching_cube_builder_1
import point_clouds_generator_plain_arrays
import point_clouds_generator_stacked_image as generator
import ext_marching_cube_metadata as metadata_debugger


def example_sq_object_from_images():
    input_paths = [
        '../images/sq-object/sq-0001.png',
        '../images/sq-object/sq-0002.png',
        '../images/sq-object/sq-0003.png',
        '../images/sq-object/sq-0004.png',
        '../images/sq-object/sq-0005.png',
        '../images/sq-object/sq-0006.png',
    ]
    xy_size = 20

    values, metadata = generator.generate(input_paths, xy_size)
    metadata_debugger.debug_metadata(metadata)

    marching_cube_builder_1.build(
        values,
        metadata,
        '../objs/sq-object.stl',
        2,
        False
    )


def example_sq_object_from_sanitised_txt():
    input_path = '../input/sq_object_sanitised.txt'
    xy_size = 21
    z_size = 8

    values, metadata = point_clouds_generator_plain_arrays.generate_by_input(input_path, xy_size, z_size)

    marching_cube_builder_1.build(
        values,
        metadata,
        '../objs/sq-object.stl',
        2,
        True
    )


if __name__ == "__main__":
    pass
