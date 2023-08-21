# Alkaline Electrolyser Specification Tool

This repository contains a Streamlit application for calculating the key performance parameters and component specifications of an alkaline electrolyser. 

The application takes user inputs for power, electrolyser efficiency, cell voltage, current density, insulation efficiency, and coolant temperature rise. Based on these inputs, it calculates the hydrogen production rate, total active surface area, water consumption rate, heat to be removed, and coolant flow rate. It also calculates the specifications for the electrodes, electrolyte, and power supply.

The application is designed to be user-friendly and provides clear, actionable results that can be used for the design and operation of alkaline electrolysers.

## Usage

You can run the application locally by cloning this repository and using the Streamlit command-line interface:

```bash
git clone https://github.com/sankalpsthakur/alkaline-electrolyser-specification-tool.git
cd alkaline-electrolyser-specification-tool
streamlit run app.py
```

## Assumptions

The model used in this application makes several key assumptions:

1. The efficiency of the electrolyser is constant at all operating conditions.
2. All the water fed into the electrolyser is converted into hydrogen and oxygen.
3. All the energy input into the electrolyser is either converted into hydrogen or lost as heat.
4. The current density across the electrode is constant.
5. Hydrogen behaves as an ideal gas at the operating conditions of the electrolyser.
6. The electrode area is uniformly distributed across all cells.
7. The only chemical reaction occurring in the electrolyser is the splitting of water into hydrogen and oxygen.
8. The properties of the coolant (such as its specific heat capacity) are constant.
9. The electrolyser is perfectly insulated, except for the heat that is deliberately removed by the cooling system.

These assumptions simplify the calculations and make the model easier to use. However, they might lead to deviations between the model predictions and actual performance of the electrolyser. These deviations should be considered when using the model for design or performance prediction of an electrolyser.

## Contributions

Contributions to this project are welcome. If you have a suggestion for improvement, please open an issue to discuss it before making a pull request.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
