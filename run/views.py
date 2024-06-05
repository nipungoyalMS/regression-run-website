from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from run.forms import RunForm
import re

# Create your views here.

import subprocess

def run(request):
    if request.method == 'POST':
        # Access form data directly from request.POST
        blocks = request.POST.get('blocks')
        project = request.POST.get('project')
        projectSetup = request.POST.get('projectSetup')
        buildPath = request.POST.get('buildPath')

        # Print all form data
        print("Blocks:", blocks)
        print("Project:", project)
        print("Project Setup:", projectSetup)
        print("Build Path:", buildPath)
        
        # You can perform further processing with the form data here
        command = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/launch_regression_run.zsh"

        if blocks:
            command += f""" -b "{blocks}" """
        if project:
            command+= f""" -programs "{project}" """
        if buildPath:
            command += f""" -build_path {buildPath} """
        if projectSetup:
            command += f""" -project_setup {projectSetup} """

        command += f""" -once"""

        print("Generated command:", command)

        # Set the path for the output file
        output_file = "/home/t-nipungoyal/Desktop/regression_run_page/regression/output"

        # Open a file to capture the output
        with open(output_file, "w") as out_file:
            # Execute the command in a new terminal window
            subprocess.run(['gnome-terminal', '--', 'bash', '-c', command], stdout=out_file, stderr=subprocess.STDOUT)

        # Return a JSON response indicating success
        return HttpResponse('Form submitted successfully')
    else:
        template = loader.get_template('run.html')
        return HttpResponse(template.render({}, request))
    

def run2(request):
    if request.method == 'POST':
        # Access form data directly from request.POST
        block = request.POST.get('block')
        project = request.POST.get('project')
        projectSetup = request.POST.get('projectSetup')
        buildPath = request.POST.get('buildPath')

        # Print all form data
        print("Block:", block)
        print("Project:", project)
        print("Project Setup:", projectSetup)
        print("Build Path:", buildPath)
        
        # You can perform further processing with the form data here
        command = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/launch_regression_run.zsh"

        if block:
            command += f""" -b "{block}" """
        if project:
            command+= f""" -programs "{project}" """
        if buildPath:
            command += f""" -build_path {buildPath} """
        if projectSetup:
            command += f""" -project_setup {projectSetup} """

        command += f""" -once"""

        print("Generated command:", command)

        # Set the path for the output file
        output_file = "/home/t-nipungoyal/Desktop/regression_run_page/regression/output"

        # Open a file to capture the output
        with open(output_file, "w") as out_file:
            # Execute the command in a new terminal window
            subprocess.run(['gnome-terminal', '--', 'bash', '-c', command], stdout=out_file, stderr=subprocess.STDOUT)

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Form submitted successfully'})
    else:
        template = loader.get_template('run2.html')
        return HttpResponse(template.render({}, request))
    
def run3(request):
    if request.method == 'POST':
        # Access form data directly from request.POST
        block = request.POST.get('block')
        project = request.POST.get('project')
        projectSetup = request.POST.get('projectSetup')
        buildPath = request.POST.get('buildPath')

        # Print all form data
        print("Block:", block)
        print("Project:", project)
        print("Project Setup:", projectSetup)
        print("Build Path:", buildPath)
        
        # You can perform further processing with the form data here
        command = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/launch_regression_run.zsh"

        if block:
            command += f""" -b "{block}" """
        if project:
            command+= f""" -programs "{project}" """
        if buildPath:
            command += f""" -build_path {buildPath} """
        if projectSetup:
            command += f""" -project_setup {projectSetup} """

        command += f""" -once"""

        print("Generated command:", command)

        # Set the path for the output file
        output_file = "/home/t-nipungoyal/Desktop/regression_run_page/regression/output"

        # Open a file to capture the output
        with open(output_file, "w") as out_file:
            # Execute the command in a new terminal window
            subprocess.run(['gnome-terminal', '--', 'bash', '-c', command], stdout=out_file, stderr=subprocess.STDOUT)

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Form submitted successfully'})
    else:
        template = loader.get_template('run3.html')
        return HttpResponse(template.render({}, request))




def extract_block_names(request):
    file_path = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/RR.list"
    block_names = set()
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'RR\d+ "blocks=(\w+)', line)
            if match:
                block_names.add(match.group(1))
    return JsonResponse({'blocks': list(block_names)})

def extract_blocks_for_project(request, project_name):
    file_path = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/RR.list"
    blocks = set()
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'RR\d+\s+"blocks\s*=\s*(\w+)\s+project\s*=\s*(\w+)', line)
            if match and match.group(2) == project_name:
                blocks.add(match.group(1))
    return JsonResponse({'blocks': list(blocks)})

def extract_project_names(request):
    file_path = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/RR.list"
    project_names = set()
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'RR\d+ "blocks=.*\sproject=([^\s]+)', line)
            if match:
                project_names.add(match.group(1))
    return JsonResponse({'projects': list(project_names)})


def extract_programs_for_block(request, block_name):
    file_path = "/home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/RR.list"
    programs = set()
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'RR\d+\s+"blocks\s*=\s*(\w+)\s+project\s*=\s*(\w+)', line)
            if match and match.group(1) == block_name:
                programs.add(match.group(2))
    return JsonResponse({'programs': list(programs)})


import os
from pathlib import Path

def get_latest_project_setup(request, project):
    if project == 'KNG':
        folder_path = '/home/scratch-kingsgate/tsmc003ffe/A0/pd/setup'
    elif project == 'BRG':
        folder_path = '/home/scratch-braga/tsmc003ffe/A0/pd/setup'
    else:
        return JsonResponse({'projectSetups': []})  # Unknown project

    # Get the list of directories and sort them by creation time
    directories = sorted(filter(os.path.isdir, Path(folder_path).iterdir()), key=os.path.getctime, reverse=True)

    # Get the names of the 5 latest directories
    latest_directories = [directory.name for directory in directories[:5]]
    return JsonResponse({'projectSetups': latest_directories})


def get_latest_build_path(request):
    folder_path = '/home/scratch-designinfra/genesys_mile/'
    # Get the list of directories and sort them by creation time
    directories = sorted(filter(os.path.isdir, Path(folder_path).iterdir()), key=os.path.getctime, reverse=True)

    # Get the names of the 5 latest directories
    latest_directories = [directory.name for directory in directories[:5]]
    return JsonResponse({'latestBuildPaths': latest_directories})


def get_project_list(request):
    try:
        # Run the command and capture its output as bytes
        command_output_bytes = subprocess.check_output(['vovproject', 'list'])
        
        # Decode the bytes to string
        command_output = command_output_bytes.decode('utf-8')
        
        # Parse the output into a list of dictionaries
        projects = []
        lines = command_output.split('\n')
        for line in lines[1:]:  # Skip the header line
            if line.strip():  # Skip empty lines
                parts = line.split()
                
                # Check if the port value is a valid integer
                try:
                    port = int(parts[3])
                except ValueError:
                    port = None
                
                project = {
                    'PROJECT': parts[0],
                    'OWNER': parts[1],
                    'HOST': parts[2],
                    'PORT': port,
                    'STATUS': parts[4]
                }
                projects.append(project)
        
        return JsonResponse({'projects': projects})
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur when running the command
        return JsonResponse({'error': str(e)}, status=500)
    
import socket
import os

def execute_commands(request):
    project_owner = request.GET.get('owner')
    try:
        print(project_owner)
        hostname = socket.gethostname()
        print(hostname)
        
        command = f'source /home/cad/setup/user/hwrc.sh; source /home/scratch-kingsgate/tsmc003ffe/A0/pd/users/nareshvijay/.aliases.nareshvijay ; vovproject list ; which ft_launch; ft_launch {project_owner}'
        print("Command:", command)
        subprocess.run(command, shell=True, check=True, executable='/bin/zsh')
        
        return HttpResponse("Commands executed successfully")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Error executing commands: {e}")


def redirect_dashboard(request):
    # Path to the file
    file_path = "/home/t-nipungoyal/Desktop/dashboard.list"

    # Initialize an empty list to store project data
    projects = []

    # Read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into project and link_to_dashboard
            parts = line.strip().split()
            project_name = parts[1].split('=')[1]
            link_to_dashboard = parts[2].split('=')[1]
            
            # Append project data to the list
            projects.append({
                'project_name': project_name,
                'link_to_dashboard': link_to_dashboard
            })

    # Return the project data as JSON response
    return JsonResponse(projects, safe=False)