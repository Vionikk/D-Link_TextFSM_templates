# D-Link_TextFSM_templates
Repository of TextFSM Templates for D-Link network devices

TextFSM is a project built by Google that takes CLI string output and passes each line through a series of regular expressions until it finds a match. The regular expressions use named capture groups to build a text table out of the significant text. The names of the capture groups are used as column headers, and the captured values are stored as rows in the table.

This templates have been tested on D-Link switches, models: DGS 3120, DES 3200, DES 3028

P.S. D-Link does not always adhere to his standards, so for example in the output of the command "show switch" for the DES 3028 switch we have a field "Clipaging", while on DGS 3120 this field is called "CLI Paging". This is one of the features of the D-Link CLI.
