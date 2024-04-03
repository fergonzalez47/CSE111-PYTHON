import math

def main():
    #1
    picnic_volume = compute_volume(6.83, 10.16);
    picnic_surface = compute_surface_area(6.83, 10.16);
    picnic = storage_efficiency(picnic_volume, picnic_surface);
    
    #1
    tall_volume = compute_volume(7.78, 11.91);
    tall_surface = compute_surface_area(7.78, 11.91);
    tall =  storage_efficiency(tall_volume, tall_surface);
    
    number2_volume = compute_volume(8.73, 11.59);
    number2_surface = compute_surface_area(8.73, 11.59);
    number2 =  storage_efficiency(number2_volume, number2_surface);
    
    number2_5_volume = compute_volume(10.32, 11.91);
    number2_5_surface = compute_surface_area(10.32, 11.91);
    number2_5 =  storage_efficiency(number2_5_volume, number2_5_surface);
    
    
    cylinder_volume = compute_volume(10.79, 17.78);
    cylinder_surface = compute_surface_area(10.79, 17.78);
    cylinder =  storage_efficiency(cylinder_volume, cylinder_surface);
    
    
    number5_volume = compute_volume(13.02, 14.29);
    number5_surface = compute_surface_area(13.02, 14.29);
    number5 =  storage_efficiency(number5_volume, number5_surface);
    
    
    number6z_volume = compute_volume(5.40, 8.89);
    number6z_surface = compute_surface_area(5.40, 8.89);
    number6z =  storage_efficiency(number6z_volume, number6z_surface);
    
    
    short_volume = compute_volume(6.83, 7.62);
    short_surface = compute_surface_area(6.83, 7.62);
    short =  storage_efficiency(short_volume, short_surface);
    
    
    number10_volume = compute_volume(15.72, 17.78);
    number10_surface = compute_surface_area(15.72, 17.78);
    number10 =  storage_efficiency(number10_volume, number10_surface);
    
    
    number211_volume = compute_volume(6.83, 12.38);
    number211_surface = compute_surface_area(6.83, 12.38);
    number211 =  storage_efficiency(number211_volume, number211_surface);
    
    number300_volume = compute_volume(7.62, 11.27);
    number300_surface = compute_surface_area(7.62, 11.27);
    number300 =  storage_efficiency(number300_volume, number300_surface);
    
    
    number303_volume = compute_volume(8.10, 11.11);
    number303_surface = compute_surface_area(8.10, 11.11);
    number303 =  storage_efficiency(number303_volume, number303_surface);
    
    
    
    
    print(f"#1 Picnic {round(picnic, 2)}");
    print(f"#1 Tall {round(tall, 2)}");
    print(f"#2 {round(number2, 2)}");
    print(f"#2.5 {round(number2_5, 2)}");
    print(f"#3 Cilinder {round(cylinder, 2)}");
    print(f"#5 {round(number5, 2)}");
    print(f"#6Z {round(number6z, 2)}");
    print(f"#8Z short {round(short, 2)}");
    print(f"#10 {round(number10, 2)}");
    print(f"#211 {round(number211, 2)}");
    print(f"#300 {round(number300, 2)}");
    print(f"#303 {round(number303, 2)}");
    
   
def storage_efficiency(volume, surfaceArea):
    return volume / surfaceArea
    
    
def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.

     Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
     Return: the volume of the cylinder
     """
    volume = math.pi * radius**2 * height
    return volume
    
    

def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surfaceArea = 2 * math.pi * radius * (radius + height)
    return surfaceArea;
    


main();