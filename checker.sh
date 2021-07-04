#!/usr/bin/env bash
# This scrip`t checks for general requirements for AirBnB project

# print_ko - Prints if a test fail in red
function print_ko()
{
	echo -e "[\033[31mFAIL\033[37m]"
}

# print_ok - Prints if a test pass in green
function print_ok()
{
    echo -e "[\033[32mPASS\033[37m]"
}

# Files used for this project
FILES=(
    README.md AUTHORS ./console.py ./models/base_model.py ./models/__init__.py
    ./models/amenity.py ./models/city.py ./models/place.py ./models/review.py
    ./models/state.py ./models/engine/file_storage.py ./models/engine/__init__.py
    ./tests/test_models/test_amenity.py ./tests/test_models/test_base_model.py
    ./tests/test_models/test_city.py ./tests/test_models/test_place.py
    ./tests/test_models/test_review.py ./tests/test_models/test_state.py
    ./tests/test_models/test_user.py ./tests/test_models/test_engine/test_file_storage.py
    ./tests/test_models/__init__.py ./tests/test_models/test_engine/__init__.py
    )

# check_file - Checks if the files exist
function check_file()
{
    echo "::::::::::::::::::::::::::::"
    echo "Checking if the file exist"
    echo "::::::::::::::::::::::::::::"
    sleep 2
    for file in "${FILES[@]}"
        do
            echo "$file"
            sleep 1
            if [ -e "$file" ]
                then
                    print_ok
            else
                print_ko
            fi
    done
}

# check_permission - Checks if the file have executable permission
function check_permission()
{
    echo "::::::::::::::::::::::::::::"
    echo "Checking if the file have executable permission"
    echo "::::::::::::::::::::::::::::"
    sleep 2
    for file in "${FILES[@]}"
        do
            echo "$file"
            sleep 1
            if [ "$file" == "README.md" ] || [ "$file" == "AUTHORS" ]
                then
                    continue
            elif [ -x "$file" ]
                then
                    print_ok
            else
                print_ko
            fi
    done
}

# check-shebang - Checks if the files contain the shebang #!/usr/bin/python3
function check_shebang()
{
    echo "::::::::::::::::::::::::::::"
    echo "Checking shebang for .py files"
    echo "::::::::::::::::::::::::::::"
    shebang="#!/usr/bin/python3"
    sleep 2
    for file in "${FILES[@]}"
        do
            if [ "$file" == "README.md" ] || [ "$file" == "AUTHORS" ]
                then
                    continue
            fi
            echo "$file"
            sleep 1
            line=$(head -1 "$file")
            if [ "$line" == "$shebang" ]
                then
                    print_ok
            else
                print_ko
            fi
    done
}
check_file
check_permission
check_shebang
