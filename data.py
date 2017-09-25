

def import_data(filename="DZIALKI.TXT"):

    with open(filename, 'r') as f:
        file = f.readlines()
        file = [data.rstrip() for data in file]
        file = [data.replace(',', '.') for data in file]
    allotment_list = []
    last_index = 3
    for line in file:
        allotment = line.split(';')
        allotment_list.append(allotment)
    return allotment_list


def get_big_small_lot():

    result = ""
    allotment_list = import_data("DZIALKI.TXT")
    biggest_lot = []
    smallest_lot = []
    acreage_index = 1
    lot_type_index = 2
    comparison_variable = 0

    for data in allotment_list[1:]:
        try:
            data[acreage_index] = float(data[acreage_index])
            if data[acreage_index] >= comparison_variable:
                comparison_variable = data[acreage_index]
                biggest_lot.append(data)
            else:
                continue
        except TypeError:
            print("Data can't be changed to float")
    biggest_lot = biggest_lot[-1][1:3]

    for data in allotment_list[1:]:
        try:
            data[acreage_index] = float(data[acreage_index])
            if comparison_variable == 0:
                comparison_variable = data[acreage_index]
            if data[acreage_index] <= comparison_variable:
                comparison_variable = data[acreage_index]
                smallest_lot.append(data)
            else:
                continue
        except TypeError:
            print("Data can't be changed to float")
    smallest_lot = smallest_lot[-1][1:3]

    result = " A: {} - {}".format(smallest_lot, biggest_lot)
    return result


def get_summary_of_data_for_parcels():

    allotment_list = import_data("DZIALKI.TXT")
    result = ""
    agricultural_parcel = 0
    agricultural_parcel_acreage = 0
    building_plot = 0
    building_plot_acreage = 0
    land_plot = 0
    land_plot_acreage = 0
    forest_parcel = 0
    forest_parcel_acreage = 0
    recreational_land = 0
    recreational_land_acreage = 0
    acreage_index = 1
    lot_type_index = 2

    for data in allotment_list[1:]:
        try:
            data[acreage_index] = float(data[acreage_index])
            if data[lot_type_index] == 'R':
                agricultural_parcel += 1
                agricultural_parcel_acreage += data[acreage_index]
            elif data[lot_type_index] == 'B':
                building_plot += 1
                building_plot_acreage += data[acreage_index]
            elif data[lot_type_index] == 'S':
                land_plot += 1
                land_plot_acreage += data[acreage_index]
            elif data[lot_type_index] == 'L':
                forest_parcel += 1
                forest_parcel_acreage += data[acreage_index]
            elif data[lot_type_index] == 'X':
                recreational_land += 1
                recreational_land_acreage += data[acreage_index]
            else:
                raise "Allotment data type Error"
        except TypeError:
            print("Data can't be changed to float")

    agricultural_parcel_acreage /= agricultural_parcel
    agricultural_parcel_acreage = round(agricultural_parcel_acreage, 2)
    building_plot_acreage /= building_plot
    building_plot_acreage = round(building_plot_acreage, 2)
    land_plot_acreage /= land_plot
    land_plot_acreage = round(land_plot_acreage, 2)
    forest_parcel_acreage /= forest_parcel
    forest_parcel_acreage = round(forest_parcel_acreage, 2)
    recreational_land_acreage /= recreational_land
    recreational_land_acreage = round(recreational_land_acreage, 2)

    result = '''\nB:                    Total     Average acreage
Agricultural parcels:   {}          {}

Building plots:         {}          {}

Land plots:             {}          {}

Forest parcels:         {}          {}

Recreational land:      {}          {}'''.format(agricultural_parcel,
agricultural_parcel_acreage,
building_plot, building_plot_acreage,
land_plot, land_plot_acreage,
forest_parcel, forest_parcel_acreage,
recreational_land,
recreational_land_acreage)
    return result


def get_total_number_of_lots_by_tax():

    allotment_list = import_data("DZIALKI.TXT")
    low_tax = 0
    medium_tax = 0
    high_tax = 0
    result = ""
    acreage_index = 1
    lot_type_index = 2
    tax_relief_index = 3

    for data in allotment_list[1:]:
        try:
            acreage_tax = 0
            tax_to_be_paid = 0
            data[acreage_index] = float(data[acreage_index])
            if data[lot_type_index] == 'R':
                acreage_tax = data[acreage_index] * 0.65
            elif data[lot_type_index] == 'B':
                acreage_tax = data[acreage_index] * 0.77
            elif data[lot_type_index] == 'S':
                acreage_tax = data[acreage_index] * 0.21
            elif data[lot_type_index] == 'L':
                acreage_tax = data[acreage_index] * 0.04
            elif data[lot_type_index] == 'X':
                acreage_tax = data[acreage_index] * 0.43

            if data[tax_relief_index] == 'A':
                tax_to_be_paid = round((acreage_tax * 20) / 100, 2)
            elif data[tax_relief_index] == 'B':
                tax_to_be_paid = round((acreage_tax * 50) / 100, 2)
            elif data[tax_relief_index] == 'C':
                tax_to_be_paid = round((acreage_tax * 90) / 100, 2)
            elif data[tax_relief_index] == 'D':
                tax_to_be_paid = round(acreage_tax, 2)

            if tax_to_be_paid <= 100:
                low_tax += 1
            elif tax_to_be_paid > 100 and tax_to_be_paid <= 500:
                medium_tax += 1
            else:
                high_tax += 1

        except TypeError:
            print("Data can't be changed to float")

    result = '''\nC:
number of lots with:

smallest tax: {},

medium tax: {},

highest tax: {}'''.format(low_tax, medium_tax, high_tax)
    return result


def export_data(filename):

    answer_a = get_big_small_lot()
    answer_b = get_summary_of_data_for_parcels()
    answer_c = get_total_number_of_lots_by_tax()
    answers = answer_a + '\n' + answer_b + '\n' + answer_c
    with open(filename, 'w') as filename:
        filename.write(answers)


def main():

    answer_a = get_big_small_lot()
    answer_b = get_summary_of_data_for_parcels()
    answer_c = get_total_number_of_lots_by_tax()
    print(answer_a, "\n", answer_b, "\n", answer_c)
    export_data("answers.txt")

main()
