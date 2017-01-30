class AppointmentsController < ApplicationController
  def new
    @appointment = Appointment.new
    @cptcodes = Cptcode.all
    @room_options= ["One room", "Two Rooms", "unknown"]
  end

  def create

    cptcodes = appointment_params[:cptcodes]

    cptstring = cptcodes.join(", ")
    p cptstring


    @appointment = Appointment.new ({procedure: appointment_params[:procedure], number_of_rooms: appointment_params[:number_of_rooms], cptstring: cptstring})

    @appointment.save
    # p @appointment
    #
    # cpt_ids = appointment_params[:cptcodes]
    # cpt_ids.each do |cpt_id|
    #   cpt = Cptcode.find(cpt_id)
    #   @appointment.cptcodes << cpt
    # end
    p @appointment

    app_hash = {pocedure: @appointment.procedure, number_of_rooms: @appointment.number_of_rooms, cptstring: @appointment.cptstring}

    require 'json'
    File.open("public/temp.json","w") do |f|
      f.write(app_hash.to_json)
    end

    redirect_to '/'
  end

  private
  def appointment_params
    params.require(:appointment).permit(:procedure, :number_of_rooms, :cptcodes => [])

  end
end
