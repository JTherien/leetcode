var twoSum = function(nums, target) {
    
    for (let i = 0, size = nums.length; i < size; i++) {

        let x = target - nums[i];

        if (nums.includes(x)) {

            if (i != nums.indexOf(x)) {

                return [i, nums.indexOf(x)]

            };
        };
    };
};

console.log(twoSum([1,2,3], 5));