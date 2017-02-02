class CptcodesController < ApplicationController
  def make_cpts
    code_list= "64479,64640,65,63650,64483,64480,64634,64635,64636,64484,20605,63685,63688,62311,62310,63661,64494,64495,64633,64490,64491,64492,64493,64450,27096".split(",")
    code_list.each do |code|
      code = Cptcode.new({name:code})
      code.save
    end

    redirect_to "appointments#new"
  end
end
