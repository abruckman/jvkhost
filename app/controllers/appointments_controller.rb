class AppointmentsController < ApplicationController
  def new
    @appointment = Appointment.new
    @procedures = ["Nerve Block","Facet Joint Injection", "Lumbar Radiofrequency","Lumbar ESI","Spinal Cord Stimulator", "Joint Injection , other" , "Lumbar Medial Branch Block", "Cervical/Thoracic Medial Branch Block","Cervical/Thoracic ESI","Cervical/Thoracic Radiofrequency"]
    @cptcodes = "64479,64640,65,63650,64483,64480,64634,64635,64636,64484,20605,63685,63688,62311,62310,63661,64494,64495,64633,64490,64491,64492,64493,64450,27096".split(",")
    @room_options= ["Unknown","One Room", "Two Rooms"]
  end

  def create

    cptcodes = appointment_params[:cptcodes]

    cptstring = cptcodes.join(", ")
    p cptstring
    app_hash = {procedure: appointment_params[:procedure], number_of_rooms: appointment_params[:number_of_rooms], cptstring: cptstring}

    @appointment = Appointment.new (app_hash)

    require 'json'
    File.open("public/temp.json","w") do |f|
      f.write(app_hash.to_json)
    end

    answer = `#{PYTHON_PATH} PicklePull.py public/temp.json`
    p answer

    @appointment.result = answer
    @appointment.save
    respond_to do |format|
      format.js{}
      format.html {redirect_to appointment_path(@appointment)}
    end
  end

  def show
    @appointment = Appointment.find(params[:id])
  end

  private
  def appointment_params
    params.require(:appointment).permit(:procedure, :number_of_rooms, :cptcodes => [])

  end
end
