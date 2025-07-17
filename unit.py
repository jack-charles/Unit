'''
@author: Jack Charles   https://jackcharlesconsulting.com/
'''

import math
import json

#_x = 1
#master unit dictionary with categories, units, and conversions to SI. Used to populate lists in various ways. 
unit_dictionary_master = {
    'Unit System': {
        'API': 'API',
        'SI': 'SI'
        },
    'Angle': {
        'degree': 1,
        'radians': 180/math.pi
        },
    'Area': {
        'acre': 4046.873,
        'cm\u00b2': 1/100**2,
        'ft\u00b2': 30.48,
        'in\u00b2': (0.3048/12)**2,
        'm\u00b2': 1,
        'mm\u00b2': 1/1000**2
        },
    'Capacity': {
        'bbl/ft': 5.615*0.3048**3/0.3048,
        'cm\u00b3/m': 1/100**3,
        'ft\u00b3/ft': 0.3048**3/0.3048,
        'gal/ft': 1/7.481*0.3048**3/0.3048,
        'in\u00b3/ft': (0.3048/12)**3/0.3048,
        'L/m': 1/1000,
        'm\u00b3/m': 1,
        'mL/m': 1/(1000/1000)
        },
    'Concentration': {
        'ppm': 1,
        'pptg': 119963.30652581
        },
    'Density Gas': {
        'g/cm\u00b3': 1000,
        'kg/m\u00b3': 1,
        'lbm/ft\u00b3': 0.45359237/0.3048**3,
        'ppg': 0.45359237*7.481/0.3048**3,
        'sg (air)': 1.225
        },
    'Density Liquid': {
        'API': lambda _dd: 1000 * 141.5 / (_dd + 131.5), 
        'g/cm\u00b3': 1000,
        'kg/m\u00b3': 1,
        'lbm/ft\u00b3': 0.45359237/0.3048**3,
        'ppg': 0.45359237*7.481/0.3048**3,
        'sg (water)': 1000
        },
    'Density Solid': {
        'g/cm\u00b3': 1000,
        'kg/m\u00b3': 1,
        'lbm/ft\u00b3': 0.45359237/0.3048**3,
        'ppg': 0.45359237*7.481/0.3048**3,
        'sg (water)': 1000
        },
    'Diameter': {
        'cm': 1/100,
        'ft': 0.3048,
        'in': (0.3048/12),
        'm': 1,
        'micron': 1/(1e6),
        'mil': 2.54e-5,
        'mm': 1/1000
        },
    'Force': {
        'klbf': 4.448222*1000,
        'kN': 1000,
        'lbf': 4.448222,
        'N': 1
        },
    'Force Large': {
        'klbf': 4.448222*1000,
        'kN': 1000,
        'ton': 9.80665*1000,
        },    
    'Length': {
        'cm': 1/100,
        'ft': 0.3048,
        'in': (0.3048/12),
        'm': 1,
        'micron': 1/(1e6),
        'mil': 2.54e-5,
        'mm': 1/1000,
        'yard': 3*0.3048
        },
    'Mass': {
        'gram': 1/1000,
        'kg': 1,
        'lbm': 0.45359237,
        'mg': 1/1e6,
        'oz': 0.02834952
        },
    'Mass Gradient': {
        'gram/m': 1/1000,
        'kg/m': 1,
        'lbm/ft': 0.45359237*0.3048,
        'mg/m': 1/1e6,
        'oz/ft': 0.02834952/0.3048
        },
    'Mass Rate': {
        'gram/day': 1/(24*60)*1/1000,
        'kg/day': 1/(24*60)*1,
        'lbm/day': 1/(24*60)*0.45359237,
        'mg/day': 1/(24*60)*1/1e6,
        'oz/day': 1/(24*60)*0.02834952,
        'gram/min': 1/1000,
        'kg/min': 1,
        'lbm/min': 0.45359237,
        'mg/min': 1/1e6,
        'oz/min': 0.02834952,
        'gram/sec': 60*1/1000,
        'kg/sec': 60*1,
        'lbm/sec': 60*0.45359237,
        'mg/sec': 60*1/1e6,
        'oz/sec': 60*0.02834952
        },
    'Permeability': {
        'Darcy': 1,
        'mD': 1/1000
        },
    'Power': {
        'BTU/hr': 0.000293,
        'hp': 0.7457,
        'kW': 1
        },
    'Pressure': {'bar': 1,
        'kPa': 1/1e2,
        'MPa': 10,
        'Pa': 1/1e5,
        'psf': 1/2088.5,
        'psi': 1/14.504
        },
    'Pressure Gradient': {
        'bar/m': 1,
        'kPa/m': 1/1e2,
        'MPa/m': 10,
        'Pa/m': 1/1e5,
        'psf/ft': 1/2088.5/0.3048,
        'psi/ft': 1/14.504/0.3048
        },
    'Temperature': {
        'C': 1,
        'F': lambda _dd: _dd * 9 / 5 + 32,
        'K': lambda _dd: _dd + 273,
        'R': lambda _dd: _dd * 9 / 5 + 491.67,
        #'FtC': (_dd - 32) * 5 / 9,
        #'KtC': _dd - 273,
        #'RtC': (_dd - 491.67) * 9 / 5
        },
    'Velocity': {'ft/min': 0.3048,
        'ft/sec': 60*0.3048,
        'm/min': 60,
        'm/sec': 1
        },
    'Viscosity': {'cP': 1,
        'Pa-sec': 1000,
        'Poise': 100,
        'lbf-sec/ft\u00b2': 47880.26,
        'lbf-sec/in\u00b2': 6894757,
        'lbm/ft-sec': 1488,
        },
    'Volume': {'bbl': 5.615*0.3048**3,
        'cm\u00b3': 1/100**3,
        'ft\u00b3': 304.8,
        'gal': 1/7.481*0.3048**3,
        'in\u00b3': (0.3048/12)**3,
        'L': 1/1000,
        'm\u00b3': 1,
        'mL': 1/(1000/1000),
        'Mscf': 1000*0.3048**3,
        'MMscf': 1e6*0.3048**3,
        'scf': 304.8,
        },
    'Volumetric Rate': {'bbl/d': 1/(24*60)*5.615*0.3048**3,
        'cm\u00b3/d': 1/(24*60)*1/100**3,
        'ft\u00b3/d': 1/(24*60)*0.3048**3,
        'gal/d': 1/(24*60)*1/7.481*0.3048**3,
        'in\u00b3/d': 1/(24*60)*(0.3048/12)**3,
        'L/d': 1/(24*60)*1/1000,
        'm\u00b3/d': 1/(24*60),
        'mL/d': 1/(24*60)*1/(1000/1000),
        'Mscf/d': 1/(24*60)*1000*0.3048**3,
        'MMscf/d': 1/(24*60)*1e6*0.3048**3,
        'scf/d': 1/(24*60)*0.3048**3,
        'bbl/min': 5.615*0.3048**3,
        'cm\u00b3/min': 1/100**3,
        'ft\u00b3/min': 304.8,
        'gal/min': 1/7.481*0.3048**3,
        'in\u00b3/min': (0.3048/12)**3,
        'L/min': 1/1000,
        'm\u00b3/min': 1,
        'mL/min': 1/(1000/1000),
        'Mscf/min': 1000*0.3048**3,
        'MMscf/min': 1e6*0.3048**3,
        'scf/min': 304.8,
        'bbl/sec': 60*5.615*0.3048**3,
        'cm\u00b3/sec': 60*1/100**3,
        'ft\u00b3/sec': 60*0.3048**3,
        'gal/sec': 60*1/7.481*0.3048**3,
        'in\u00b3/sec': 60*(0.3048/12)**3,
        'L/sec': 60*1/1000,
        'm\u00b3/sec': 60*1,
        'mL/sec': 60*1/(1000/1000),
        'Mscf/sec': 60*1000*0.3048**3,
        'MMscf/sec': 60*1e6*0.3048**3,
        'scf/sec': 60*0.3048**3
        } 
    }

unit_convert_dictionary = {
        'degree': 1,
        'radians': 180/math.pi,
        'acre': 4046.873,
        'cm\u00b2': 1/100**2,
        'ft\u00b2': 0.3048**2,
        'in\u00b2': (0.3048/12)**2,
        'm\u00b2': 1,
        'mm\u00b2': 1/1000**2,
        'bbl/ft': 5.615*0.3048**3/0.3048,
        'cm\u00b3/m': 1/100**3,
        'ft\u00b3/ft': 0.3048**3/0.3048,
        'gal/ft': 1/7.481*0.3048**3/0.3048,
        'in\u00b3/ft': (0.3048/12)**3/0.3048,
        'L/m': 1/1000,
        'm\u00b3/m': 1,
        'mL/m': 1/(1000/1000),
        'ppm': 1,
        'pptg': 119963.30652581,
        'kg/m\u00b3': 1,
        'lbm/ft\u00b3': 0.45359237/0.3048**3,
        'ppg': 0.45359237*7.481/0.3048**3,
        'sg (air)': 1.225,
        'API': lambda _dd: 141.5 / (_dd + 131.5),
        'g/cm\u00b3': 1000,
        'kg/m\u00b3': 1,
        'lbm/ft\u00b3': 0.45359237/0.3048**3,
        'ppg': 0.45359237*7.481/0.3048**3,
        'sg (water)': 1,
        'g/cm\u00b3': 1000,
        'kg/m\u00b3': 1,
        'lbm/ft\u00b3': 0.45359237/0.3048**3,
        'ppg': 0.45359237*7.481/0.3048**3,
        'sg (water)': 1,
        'cm': 1/100,
        'ft': 0.3048,
        'in': (0.3048/12),
        'm': 1,
        'micron': 1/(1e6),
        'mil': 2.54e-5,
        'yard': 3*0.3048,
        'mm': 1/1000,
        'klbf': 4.448222*1000,
        'kN': 1000,
        'lbf': 4.448222,
        'N': 1,
        'gram': 1/1000,
        'kg': 1,
        'lbm': 0.45359237,
        'mg': 1/1e6,
        'oz': 0.02834952,
        'gram/m': 1/1000,
        'kg/m': 1,
        'lbm/ft': 0.45359237*0.3048,
        'mg/m': 1/1e6,
        'oz/ft': 0.02834952/0.3048,
        'gram/day': 1/(24*60)*1/1000,
        'kg/day': 1/(24*60)*1,
        'lbm/day': 1/(24*60)*0.45359237,
        'mg/day': 1/(24*60)*1/1e6,
        'oz/day': 1/(24*60)*0.02834952,
        'gram/min': 1/1000,
        'kg/min': 1,
        'lbm/min': 0.45359237,
        'mg/min': 1/1e6,
        'oz/min': 0.02834952,
        'gram/sec': 60*1/1000,
        'kg/sec': 60*1,
        'lbm/sec': 60*0.45359237,
        'mg/sec': 60*1/1e6,
        'oz/sec': 60*0.02834952,
        'Darcy': 1,
        'mD': 1/1000,
        'BTU/hr': 0.000293,
        'hp': 0.7457,
        'kW': 1,
        'bar': 1,
        'kPa': 1/1e2,
        'MPa': 10,
        'Pa': 1/1e5,
        'psf': 1/2088.5,
        'psi': 1/14.504,
        'bar/m': 1,
        'kPa/m': 1/1e2,
        'MPa/m': 10,
        'Pa/m': 1/1e5,
        'psf/ft': 1/2088.5/0.3048,
        'psi/ft': 1/14.504/0.3048,
        'CtC': lambda _dd: _dd * 1,
        'FtC': lambda _dd: (_dd - 32) * 5 / 9,
        'KtC': lambda _dd: _dd - 273,
        'RtC': lambda _dd: (_dd - 491.67) * 9 / 5,
        'CtF': lambda _dd: _dd * 9 / 5 + 32,
        'CtK': lambda _dd: _dd + 273,
        'CtR': lambda _dd: _dd * 9 / 5 + 491.67,
        'ft/min': 0.3048,
        'ft/sec': 60*0.3048,
        'm/min': 60,
        'm/sec': 1,
        'cP': 1,
        'Pa-sec': 1000,
        'Poise': 100,
        'lbf-sec/ft\u00b2': 47880.26,
        'lbf-sec/in\u00b2': 6894757,
        'lbm/ft-sec': 1488,
        'bbl': 5.615*0.3048**3,
        'cm\u00b3': 1/100**3,
        'ft\u00b3': 0.3048**3,
        'gal': 1/7.481*0.3048**3,
        'in\u00b3': (0.3048/12)**3,
        'L': 1/1000,
        'm\u00b3': 1,
        'mL': 1/(1000/1000),
        'Mscf': 1000*0.3048**3,
        'MMscf': 1e6*0.3048**3,
        'scf': 0.3048**3,
        'bbl/d': 1/(24*60)*5.615*0.3048**3,
        'cm\u00b3/d': 1/(24*60)*1/100**3,
        'ft\u00b3/d': 1/(24*60)*0.3048**3,
        'gal/d': 1/(24*60)*1/7.481*0.3048**3,
        'in\u00b3/d': 1/(24*60)*(0.3048/12)**3,
        'L/d': 1/(24*60)*1/1000,
        'm\u00b3/d': 1/(24*60),
        'mL/d': 1/(24*60)*1/(1000/1000),
        'Mscf/d': 1/(24*60)*1000*0.3048**3,
        'MMscf/d': 1/(24*60)*1e6*0.3048**3,
        'scf/d': 1/(24*60)*0.3048**3,
        'bbl/min': 5.615*0.3048**3,
        'cm\u00b3/min': 1/100**3,
        'ft\u00b3/min': 0.3048**3,
        'gal/min': 1/7.481*0.3048**3,
        'in\u00b3/min': (0.3048/12)**3,
        'L/min': 1/1000,
        'm\u00b3/min': 1,
        'mL/min': 1/(1000/1000),
        'Mscf/min': 1000*0.3048**3,
        'MMscf/min': 1e6*0.3048**3,
        'scf/min': 0.3048**3,
        'bbl/sec': 60*5.615*0.3048**3,
        'cm\u00b3/sec': 60*1/100**3,
        'ft\u00b3/sec': 60*0.3048**3,
        'gal/sec': 60*1/7.481*0.3048**3,
        'in\u00b3/sec': 60*(0.3048/12)**3,
        'L/sec': 60*1/1000,
        'm\u00b3/sec': 60*1,
        'mL/sec': 60*1/(1000/1000),
        'Mscf/sec': 60*1000*0.3048**3,
        'MMscf/sec': 60*1e6*0.3048**3,
        'scf/sec': 60*0.3048**3
        }

API_unitsystem = {
    'Unit System': 'API',
    'Angle': 'degree',
    'Area': 'ft\u00b2',
    'Capacity': 'bbl/ft',
    'Concentration': 'pptg',
    'Density Gas': 'sg (air)',
    'Density Liquid': 'ppg',
    'Density Solid': 'ppg',
    'Diameter': 'in',
    'Force': 'lbf',
    'Length': 'ft',
    'Mass': 'lbm',
    'Mass Gradient': 'lbm/ft',
    'Mass Rate': 'lbm/min',
    'Permeability': 'mD',
    'Power': 'hp',
    'Pressure': 'psi',
    'Pressure Gradient': 'psi/ft',
    'Temperature': 'F',
    'Velocity': 'ft/sec',
    'Viscosity': 'cP',
    'Volume': 'bbl',
    'Volumetric Rate': 'bbl/min'
    }

metric_unitsystem = {
    'Unit System': 'metric',
    'Angle': 'degree',
    'Area': 'm\u00b2',
    'Capacity': 'bbl/ft',
    'Concentration': 'ppm',
    'Density Gas': 'sg (air)',
    'Density Liquid': 'kg/m\u00b3',
    'Density Solid': 'kg/m\u00b3',
    'Diameter': 'cm',
    'Force': 'kN',
    'Length': 'm',
    'Mass': 'kg',
    'Mass Gradient': 'kg/m',
    'Mass Rate': 'kg/min',
    'Permeability': 'mD',
    'Power': 'kW',
    'Pressure': 'kPa',
    'Pressure Gradient': 'kPa/m',
    'Temperature': 'C',
    'Velocity': 'm/sec',
    'Viscosity': 'cP',
    'Volume': 'm\u00b3',
    'Volumetric Rate': 'm\u00b3/min'
    }

unitsystem_dictionary = {'API': API_unitsystem, 'SI': metric_unitsystem}

class UnitSystem():
    def __init__(self, name_unitsystem, angle, area, capacity, concentration, density_gas, density_liquid, density_solid, 
                 diameter, force, length, mass, mass_gradient, mass_rate, permeability, power, pressure, 
                 pressure_gradient, temperature, velocity, viscosity, volume, volumeteric_rate): 
        self.name_unitsystem = name_unitsystem
        self.angle = angle
        self.area = area
        self.capacity = capacity
        self.concentration = concentration
        self.density_gas = density_gas
        self.density_liquid = density_liquid
        self.density_solid = density_solid
        self.diameter = diameter
        self.force = force
        self.length = length
        self.mass = mass
        self.mass_gradient = mass_gradient
        self.mass_rate = mass_rate
        self.permeability = permeability
        self.power = power
        self.pressure = pressure
        self.pressure_gradient = pressure_gradient
        self.temperature = temperature
        self.velocity = velocity
        self.viscosity = viscosity
        self.volume = volume
        self.volumetric_rate = volumeteric_rate

def import_units_json(data_filename):
    with open(data_filename, 'r',) as file:
        data_dictionary = json.load(file)
    
    #unit_class = UnitSystemClass(**data_dictionary)      #this would work if the class names were identical to the dictionary
    _dd = data_dictionary
    unit_class = UnitSystem(_dd['Unit System'], _dd['Angle'], _dd['Area'], _dd['Capacity'], _dd['Concentration'], 
                            _dd['Density Gas'], _dd['Density Liquid'], _dd['Density Solid'], _dd['Diameter'], _dd['Force'], 
                            _dd['Length'], _dd['Mass'],_dd['Mass Gradient'], _dd['Mass Rate'], _dd['Permeability'], 
                            _dd['Power'], _dd['Pressure'], _dd['Pressure Gradient'], _dd['Temperature'], _dd['Velocity'], 
                            _dd['Viscosity'], _dd['Volume'], _dd['Volumetric Rate'])
    return unit_class

def export_units_json(unit_class, data_filename):
    data_dictionary = {'Unit System': unit_class.name_unitsystem, 'Angle': unit_class.angle, 'Area': unit_class.area, 'Capacity': unit_class.capacity, 'Concentration': unit_class.concentration, 
                       'Density Gas': unit_class.density_gas, 'Density Liquid': unit_class.density_liquid, 'Density Solid': unit_class.density_solid, 'Diameter': unit_class.diameter, 'Force': unit_class.force, 
                       'Length': unit_class.length, 'Mass': unit_class.mass, 'Mass Gradient': unit_class.mass_gradient, 'Mass Rate': unit_class.mass_rate, 'Permeability': unit_class.permeability, 
                       'Power': unit_class.power, 'Pressure': unit_class.pressure, 'Pressure Gradient': unit_class.pressure_gradient, 'Temperature': unit_class.temperature, 'Velocity': unit_class.velocity, 
                       'Visocisty': unit_class.viscosity, 'Volume': unit_class.volume, 'Volumetric Rate': unit_class.volumetric_rate}
    
    with open(data_filename, 'w',) as file:
        json.dump(data_dictionary, file)
    return

def convert(value, x_unit, y_unit):   
    #value, original unit, unit to convert to  
    #multiply variable by key-value to convert units to internal SI system. Reciprocal of dictionary will be used to convert from SI to new unit
    #temperature is special case, calls lambda function
    
    try:
        if (x_unit and y_unit) in list(unit_convert_dictionary.keys()) :
            converted_value = value * unit_convert_dictionary[x_unit] / unit_convert_dictionary[y_unit]
        elif x_unit is y_unit:
            converted_value = value
        elif str(x_unit+"tC") in list(unit_convert_dictionary.keys()):
            converted_value_temp = unit_convert_dictionary[str(x_unit+"tC")](value)
            converted_value = unit_convert_dictionary[str("Ct"+y_unit)](converted_value_temp)
        else:
            converted_value = None
            print(f"{x_unit} or {y_unit} not found")
    except:
        converted_value = 0
        print(f"Error converting {value} {x_unit} to {y_unit}")
    #debugging use
    #print(list(unit_convert_dictionary.keys()))
    #print(f"Check: {value} {x_unit} {unit_convert_dictionary[x_unit]} is {converted_value} {y_unit} {unit_convert_dictionary[y_unit]}")
    return converted_value