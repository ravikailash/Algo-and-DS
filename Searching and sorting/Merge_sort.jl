# Merge sort


# Function to merge the partitions
function merge_slices(a, b)
    i, j = 1, 1;
    result = Int8[];
    while i <= length(a) && j <= length(b)
        if a[i] < b[j]
            push!(result, a[i])
            i += 1
        else
            push!(result, b[j])
            j += 1
        end
    end
    if i <= length(a)
        append!(result, a[i:length(a)])
    end
    if j <= length(b)
        append!(result, b[j:length(b)])
    end 
    return result; 
end


# Function for the main sorting
function merge_sort(a)
    if length(a) == 1
        return a
    end
    mid = trunc(Int, length(a)/2);
    left = merge_sort(a[1:mid]);
    right = merge_sort(a[mid+1:length(a)]);
    return merge_slices(left, right)
end

arr1 = [3, 7, 4, 6, 1, 9];
arr2 = [10, 20, 1, 8, 2, 5, 0]
println(arr1);
println(merge_sort(arr1))

println(arr2)
println(merge_sort(arr2))

# Appending arr2 to arr1 and sorting it
println(append!(arr1, arr2));
println(merge_sort(arr1));
