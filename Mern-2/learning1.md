# Learning one 
## What is a server?
- Server is used for store the data and fetch the data
- Server is actively running and listening for your requests to execute some function


> # merN --> Node.JS 
> ## What is the node js ?
>
> - Node js is a Runtime Where the JavaScript Code is/will be executed.
> - Who uses NodeJS? 
>   - NodeJS used by famous companies like X(formarly Twitter), Netflix, PayPal, Uber etc...
> - NodeJS is used for server side rendering which is for Backend development.
-------------------------------------------------------------------------------------------------------------

> # NPM (Node Package Manager)
> - It is a CLI(Command Line Interface) Tool Where it used for Publishing and Downloading Packages
> - How NPM downloads or installs packages?
>   - It downloads packages by requesting them from [npm.org](https://www.npmjs.com/)


# Mongoose Operators
Comparison Operators:
Equality:

$eq: Matches values that are equal.
$ne: Matches values that are not equal.
Comparison:

$gt: Matches values that are greater than.
$lt: Matches values that are less than.
$gte: Matches values that are greater than or equal to.
$lte: Matches values that are less than or equal to.
Logical:

$and: Joins query clauses with a logical AND.
$or: Joins query clauses with a logical OR.
$not: Inverts the effect of a query expression.
Element Operators:
Existence:

$exists: Matches documents that have the specified field.
Type:

$type: Selects documents if a field is of the specified type.
Evaluation Operators:
Modulus:

$mod: Performs a modulo operation on the value of a field.
Text Search:

$text: Performs text search.
Where:

$where: Matches documents that satisfy a JavaScript expression.
Array Operators:
Equality:

$elemMatch: Matches documents with an array field containing at least one element that matches all the specified criteria.
Size:

$size: Matches documents where the array field is a specific size.
Projection:

$slice: Projects elements from an array.
Geospatial Operators:
Near:

$near: Returns geospatial objects in proximity to a point.
Within:

$geoWithin: Selects geometries within a bounding GeoJSON geometry.
Array Update Operators:
Push:

$push: Appends a specified value to an array.
Pull:

$pull: Removes all occurrences of a value from an array.
Filter:

$filter: Filters the elements of an array based on a condition.
Bitwise Operators:
And:

$bit: Performs bitwise AND.
Or:

$bit: Performs bitwise OR.
Projection Operators:
Include Fields:

$project: Specifies the fields to include or exclude from the query result.
Rename Fields:

$rename: Renames fields in a document.

## Important links
- [flavio](https://flaviocopes.com/)