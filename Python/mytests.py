#test data quality in columns of a database

from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_for_min_max
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import check_for_duplicates


test1={
	"testname":"Check for nulls",
	"test":check_for_nulls,
	"column": "monthid",
	"table": "DimMonth"
}


test2={
	"testname":"Check for min and max",
	"test":check_for_min_max,
	"column": "monthid",
	"table": "DimMonth",
	"minimum":1,
	"maximum":12
}


test3={
	"testname":"Check for valid values",
	"test":check_for_valid_values,
	"column": "category",
	"table": "DimCustomer",
	"valid_values":{'Individual','Company'}
}


test4={
	"testname":"Check for duplicates",
	"test":check_for_duplicates,
	"column": "monthid",
	"table": "DimMonth"
}

test7={
    "testname":"Check for valid values",
    "test":check_for_valid_values,
    "column": "quartername",
    "table": "DimMonth",
    "valid_values":{'Q1','Q2','Q3','Q4'}
}

test8={
    "testname":"Check for duplicates",
    "test":check_for_duplicates,
    "column": "customerid",
    "table": "DimCustomer"
}

test9={
	"testname":"Check for nulls",
	"test":check_for_nulls,
	"column": "billedamount",
	"table": "FactBilling"
}

test10={
    "testname":"Check for duplicates",
    "test":check_for_duplicates,
    "column": "billid",
    "table": "FactBilling"
}

test11={
    "testname":"Check for valid values",
    "test":check_for_valid_values,
    "column": "quarter",
    "table": "DimMonth",
    "valid_values":{'1','2','3','4'}
}