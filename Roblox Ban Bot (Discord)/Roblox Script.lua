local Data = require(game:GetService("ServerScriptService"):WaitForChild('000Webhost')) -- Change 000Webhost to the name of the module script
local Players = game:GetService("Players")


Players.PlayerAdded:Connect(function(player)
	while wait(5) do
		local IsBanned = Data:Get("Bans", player.UserId)
		if IsBanned == "true" then
			player:Kick("You've been banned from this game!")
		else
			--warn("User is not banned!")
		end
	end
end)







