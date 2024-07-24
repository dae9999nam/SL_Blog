EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Simple LED Circuit"
Date "2024-06-03"
Rev "1"
Comp "The University of Hong Kong"
Comment1 "Drawn by: Baek Seunghyeon"
Comment2 "Student ID: 3035821659"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:Battery BT1
U 1 1 665D228B
P 6550 3950
F 0 "BT1" H 6658 3996 50  0000 L CNN
F 1 "103(CR2032)" H 6658 3905 50  0000 L CNN
F 2 "SimpleLED:BatteryHolder_Keystone_103_1x20mm" V 6550 4010 50  0001 C CNN
F 3 "~" V 6550 4010 50  0001 C CNN
	1    6550 3950
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D1
U 1 1 665D4011
P 6050 4300
F 0 "D1" H 6043 4045 50  0000 C CNN
F 1 "Red" H 6043 4136 50  0000 C CNN
F 2 "LED_SMD:LED_1210_3225Metric" H 6050 4300 50  0001 C CNN
F 3 "~" H 6050 4300 50  0001 C CNN
	1    6050 4300
	-1   0    0    1   
$EndComp
$Comp
L Device:R R1
U 1 1 665D4D6D
P 6100 3600
F 0 "R1" V 5893 3600 50  0000 C CNN
F 1 "300R" V 5984 3600 50  0000 C CNN
F 2 "Resistor_SMD:R_1206_3216Metric" V 6030 3600 50  0001 C CNN
F 3 "~" H 6100 3600 50  0001 C CNN
	1    6100 3600
	0    1    1    0   
$EndComp
Wire Wire Line
	6250 3600 6550 3600
Wire Wire Line
	6550 3600 6550 3750
Wire Wire Line
	6550 4300 6550 4150
Wire Wire Line
	6200 4300 6550 4300
Wire Wire Line
	5950 3600 5600 3600
Wire Wire Line
	5600 3600 5600 3750
Wire Wire Line
	5600 4150 5600 4300
Wire Wire Line
	5600 4300 5900 4300
$Comp
L Switch:SW_Push SW1
U 1 1 665D60ED
P 5600 3950
F 0 "SW1" H 5600 4235 50  0000 C CNN
F 1 "SW_Push" H 5600 4144 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_SPST_CK_RS282G05A3" H 5600 4150 50  0001 C CNN
F 3 "~" H 5600 4150 50  0001 C CNN
	1    5600 3950
	0    -1   -1   0   
$EndComp
$Comp
L Mechanical:MountingHole H1
U 1 1 665DD3CD
P 6050 4700
F 0 "H1" H 6150 4746 50  0000 L CNN
F 1 "MountingHole" H 6150 4655 50  0000 L CNN
F 2 "MountingHole:MountingHole_4mm" H 6050 4700 50  0001 C CNN
F 3 "~" H 6050 4700 50  0001 C CNN
	1    6050 4700
	1    0    0    -1  
$EndComp
$EndSCHEMATC
