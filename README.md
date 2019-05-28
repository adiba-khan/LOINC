# Access LOINC through the HL7 FHIR API
Access the API (beta status) to extract descriptions of LOINC codes.

LOINC is a set of standard terminology for various medical contexts. It is prevalent for coding laboratory measurements. 

Credentials are needed to access the API and can be obtained for free (https://loinc.org/).
This Python script takes a LOINC code (i.e. 4544-3) as input and returns the string description (Hematocrit [Volume Fraction] of Blood by Automated count).
