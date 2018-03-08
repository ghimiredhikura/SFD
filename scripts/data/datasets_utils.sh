function create_folder {
    root_dir=$1
    folder_name=$2

    if [[ -z $root_dir ]]
    then
        echo "You must provide a valid root directory where to create the folder"
        exit 1
    fi

    if [[ -z $folder_name ]]
    then
        echo "You must provide a valid folder name"
        exit 1
    fi

    output_dir=${root_dir}/${folder_name}
    mkdir -p $output_dir
    echo $output_dir
}


function invalid_option {
    # $1 is the OPTARG that was wrong
    # $2 is the script name ($0)
    echo "Invalid option: -$1" >&2
    echo "Execute:"
    echo "$2 -h"
    echo "to read a list of valid parameters."
}
