--[[


███████████████████████████████████████████████▀█
█▄─█▀▀▀█─▄██▀▄─██▄─▄▄▀█▄─▀█▄─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█
██─█─█─█─███─▀─███─▄─▄██─█▄▀─███─███─█▄▀─██─██▄─█
▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀

	Do not share your webhost url!
--]]


--** Configuration
local hostUrl = "" -- Your 000webhost url!


--** Variables
local HttpService = game:GetService("HttpService")


local Webhost = {}


function Webhost:Create(name)
	local url =  hostUrl.."create.php?name="..name
	local returndata = HttpService:GetAsync(url)
	if returndata == "" then
		local success = warn("New database created: "..name)
	else
		local createerror = warn(name.." database couldn't be created maybe this database name has already been used?")
	end
end


function Webhost:Update(database, key, value)
	local url = hostUrl.."update.php?database="..database.."&key="..key.."&value="..value
	local returndata = HttpService:GetAsync(url)
	if returndata == "Updated" then
		return returndata
	else
		local updateerror = warn(key.." data couldn't be updated!")
		return updateerror
	end
end

function Webhost:Get(database, key)
	local url = hostUrl.."get.php?database="..database.."&key="..key
	--warn(url)
	local returndata = HttpService:GetAsync(url)
	if returndata == "No data" then
		local geterror = warn("Couldn't find data for the key "..key)
		return geterror
	else
		local success = returndata
		return success
	end
	
end


return Webhost
