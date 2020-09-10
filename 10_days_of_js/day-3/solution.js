/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    var grande = nums[0];
    var segundoGrande = nums[0];

    for (var i = 1; i < nums.length; i++) {
        if (nums[i] > grande) {
            segundoGrande = grande;
            grande = nums[i];
            continue;
        }
        if ((nums[i] > segundoGrande) && (nums[i] < grande)) {
            segundoGrande = nums[i];
        }   
    }
    return segundoGrande;
    }
